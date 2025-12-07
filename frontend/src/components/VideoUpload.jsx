import React, { useState } from "react";
import axios from "axios";
import Result from "./Result";

export default function VideoUpload() {
  const [video, setVideo] = useState(null);
  const [result, setResult] = useState(null);

  const analyzeVideo = async () => {
    if (!video) return;

    const formData = new FormData();
    formData.append("file", video);

    const response = await axios.post(
      "http://127.0.0.1:8000/analyze-video",
      formData,
      { headers: { "Content-Type": "multipart/form-data" } }
    );

    setResult(response.data);
  };

  return (
    <div className="card">
      <h2>Analyze Video</h2>
      <input
        type="file"
        accept="video/*"
        onChange={(e) => setVideo(e.target.files[0])}
      />
      <button onClick={analyzeVideo}>Analyze Video</button>

      {result && <Result data={result} />}
    </div>
  );
}
