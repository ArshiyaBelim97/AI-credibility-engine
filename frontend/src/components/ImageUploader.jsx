import React, { useState } from "react";
import axios from "axios";
import Result from "./Result";

export default function ImageUpload() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setImage(e.target.files[0]);
  };

  const analyzeImage = async () => {
    if (!image) return;

    const reader = new FileReader();
    reader.onloadend = async () => {
      const base64 = reader.result.split(",")[1];

      const response = await axios.post("http://127.0.0.1:8000/analyze-image", {
        image_base64: base64,
      });

      setResult(response.data);
    };

    reader.readAsDataURL(image);
  };

  return (
    <div className="card">
      <h2>Analyze Image</h2>
      <input type="file" accept="image/*" onChange={handleChange} />
      <button onClick={analyzeImage}>Analyze Image</button>

      {result && <Result data={result} />}
    </div>
  );
}
