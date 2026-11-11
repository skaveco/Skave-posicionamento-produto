"""Converte artboards .dc.html (templates estáticos do brand kit Ritter) em HTML puro e PNG via Chrome headless."""
import html as _html, json, os, re, shutil, subprocess, sys, pathlib
# Chrome: variável CHROME, depois o do PATH (Linux, sessões na nuvem), depois o do Mac.
CHROME = os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium") or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PALETTE = {
    "dark":  {"bg": "#2F3B2F", "txt": "#F8F8F6", "sup": "#ABB9AB", "line": "#445644", "soft": "#3A4A3A"},
    "light": {"bg": "#F3F3E7", "txt": "#252F25", "sup": "#667266", "line": "#D7D7C9", "soft": "#E4E4D2"},
}
def convert(src, blobs, mode_override=None):
    s = src.read_text(encoding="utf-8")
    helmet = re.search(r"<helmet>(.*?)</helmet>", s, re.S).group(1)
    body = re.search(r"</helmet>(.*?)</x-dc>", s, re.S).group(1)
    # O editor do canvas pode salvar data-props entre aspas duplas, com &quot;.
    m = re.search(r"data-props='(.*?)'", s, re.S) or re.search(r'data-props="(.*?)"', s, re.S)
    props = json.loads(_html.unescape(m.group(1)))
    mode = mode_override or props.get("mode", {}).get("default", "light")
    vals = dict(PALETTE[mode])
    # TWICH usa fundo primário
    if "Twich" in src.name or "twich" in src.name.lower():
        vals["bg"] = "#252F25" if mode == "dark" else "#F8F8F6"
    for k, v in vals.items():
        body = re.sub(r"\{\{\s*%s\s*\}\}" % k, v, body)
    left = re.findall(r"\{\{[^}]*\}\}", body)
    if left: raise SystemExit(f"{src.name}: holes sem valor {left}")
    for blob, local in blobs.items():
        body = body.replace(f"/_blob/{blob}", pathlib.Path(local).as_uri())
    w = props["$preview"]["width"]; h = props["$preview"]["height"]
    html = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>{helmet}</head><body>{body}</body></html>"
    return html, w, h, mode
def main():
    src_dir, out_dir, blobs_json = sys.argv[1], sys.argv[2], sys.argv[3]
    blobs = json.loads(blobs_json)
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    for i, f in enumerate(sys.argv[4:], 1):
        html, w, h, mode = convert(pathlib.Path(src_dir) / f, blobs)
        hp = out / f"{i:02d}.html"; hp.write_text(html, encoding="utf-8")
        png = out / f"{i:02d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--window-size={w},{h}", "--virtual-time-budget=8000", "--allow-file-access-from-files",
                        f"--screenshot={png}", hp.as_uri()], check=True, capture_output=True)
        print(png.name, mode)
main()
