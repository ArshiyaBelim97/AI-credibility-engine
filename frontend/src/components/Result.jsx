import React from "react";

export default function Result({ data }) {
  return (
    <div className="result-box">
      <h3>Result</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
