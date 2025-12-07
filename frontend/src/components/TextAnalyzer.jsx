import React, { useState } from "react";

export default function TextAnalyzer() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeText = async () => {
    const response = await fetch("http://127.0.0.1:8000/analyze-text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div>
      <h2>Text Detector</h2>

      <textarea
        placeholder="Paste text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={6}
        style={{ width: "100%" }}
      />

      <button onClick={analyzeText}>Analyze</button>

      {result && (
        <pre style={{ marginTop: "20px" }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
