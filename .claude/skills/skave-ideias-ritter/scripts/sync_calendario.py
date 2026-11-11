"""Gera os registros do Calendário de conteúdos a partir dos conteudo.md.

Uso:
    python3 -I sync_calendario.py "<pasta Conteúdos de posts>" "<pasta de saída>"

Lê todos os conteudo.md abaixo da pasta de posts e grava, na pasta de saída,
um JSON por publicação (<doc_id>.json) e um manifest.json com a lista de
doc_ids e caminhos. Os JSONs são enviados ao banco do calendário com a ação
"batch" do ArtifactData (coleção "posts"), um "set" por arquivo.
"""
import datetime as dt
import json
import pathlib
import re
import sys
import unicodedata

MESES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
     "agosto", "setembro", "outubro", "novembro", "dezembro"], 1)}
CAMPOS = ["titulo", "data", "rede", "formato", "funil", "pilar", "dor", "status",
          "producao", "template", "modo_cor", "link_arte"]


def nfc(s):
    return unicodedata.normalize("NFC", s)


def slug(s, n=48):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > n:
        s = s[:n + 1].rsplit("-", 1)[0]
    return s or "post"


def data_iso(texto):
    m = re.match(r"\s*(\d{1,2}) de ([A-Za-zçÇ]+),? (\d{4})", nfc(texto or ""))
    if not m:
        raise ValueError(f"data fora do padrão '16 de Novembro, 2026': {texto!r}")
    mes = MESES.get(m.group(2).lower())
    if not mes:
        raise ValueError(f"mês desconhecido: {m.group(2)!r}")
    return f"{int(m.group(3)):04d}-{mes:02d}-{int(m.group(1)):02d}"


def ler(md, raiz):
    s = nfc(md.read_text(encoding="utf-8"))
    fm = re.match(r"---\n(.*?)\n---\n?(.*)", s, re.S)
    if not fm:
        raise ValueError(f"{md}: sem frontmatter")
    meta = {}
    for linha in fm.group(1).splitlines():
        if ":" in linha:
            k, v = linha.split(":", 1)
            meta[k.strip()] = v.strip()
    corpo = fm.group(2)
    texto = re.search(r"^## Texto publicável\s*\n(.*?)(?=^## |\Z)", corpo, re.S | re.M)
    doc = {k: meta.get(k, "") for k in CAMPOS}
    doc["data"] = data_iso(meta.get("data", ""))
    doc["status"] = (doc["status"] or "rascunho").lower()
    doc["texto"] = texto.group(1).strip() if texto else ""
    legenda = re.search(r"^## Legenda\s*\n(.*?)(?=^## |\Z)", corpo, re.S | re.M)
    doc["legenda"] = legenda.group(1).strip() if legenda else ""
    pasta = md.parent
    arte = pasta / "arte"
    doc["artes"] = len(list(arte.glob("*.png"))) if arte.is_dir() else 0
    doc["pasta"] = nfc(str(pasta.relative_to(raiz.parent)))
    mtime = max([md.stat().st_mtime] + [p.stat().st_mtime for p in arte.glob("*.png")] if arte.is_dir() else [md.stat().st_mtime])
    doc["atualizado_em"] = dt.datetime.fromtimestamp(mtime, dt.timezone.utc).isoformat(timespec="seconds")
    doc_id = f"{doc['data']}-{slug(doc['formato'], 12)}-{slug(doc['titulo'])}"
    return doc_id, doc


def main():
    raiz = pathlib.Path(sys.argv[1]).resolve()
    out = pathlib.Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    manifest, erros = [], []
    for md in sorted(raiz.rglob("conteudo.md")):
        try:
            doc_id, doc = ler(md, raiz)
        except ValueError as e:
            erros.append(str(e))
            continue
        if any(m["doc_id"] == doc_id for m in manifest):
            erros.append(f"doc_id repetido: {doc_id} ({md})")
            continue
        f = out / f"{doc_id}.json"
        f.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        manifest.append({"doc_id": doc_id, "file_path": str(f), "status": doc["status"], "data": doc["data"]})
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"posts": len(manifest), "erros": erros, "manifest": str(out / "manifest.json")}, ensure_ascii=False, indent=2))
    for m in manifest:
        print(m["doc_id"], m["status"], sep="\t")


if __name__ == "__main__":
    main()
