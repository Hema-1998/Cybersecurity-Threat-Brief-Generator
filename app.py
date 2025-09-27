from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def chunk(text, max_len=800):
    words, out, buf = text.split(), [], []
    for w in words:
        buf.append(w)
        if sum(len(x) for x in buf) > max_len:
            out.append(" ".join(buf)); buf = []
    if buf: out.append(" ".join(buf))
    return out

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/brief", methods=["POST"])
def brief():
    text = request.json.get("text","").strip()
    if not text:
        return jsonify(error="No text provided"), 400

    parts = chunk(text)
    summaries = [summarizer(p, max_length=120, min_length=40, do_sample=False)[0]["summary_text"]
                 for p in parts]
    combined = " ".join(summaries)
    final = summarizer(combined, max_length=120, min_length=40, do_sample=False)[0]["summary_text"]

    impact = ""
    mitigation = ""
    lower = text.lower()
    if "affect" in lower or "affected" in lower or "impact" in lower:
        impact = "Affected systems/components mentioned in the advisory; review versions and environments."
    if "mitigat" in lower or "patch" in lower or "upgrade" in lower or "workaround" in lower:
        mitigation = "Apply vendor patches/updates immediately; restrict exposure; monitor logs/IPS."

    return jsonify(summary=final, impact=impact, mitigation=mitigation)

if __name__ == "__main__":
    app.run(debug=True)
