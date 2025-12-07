import React, { useState } from "react";
import ImageUploader from "./components/ImageUploader";
import TextAnalyzer from "./components/TextAnalyzer.jsx";

export default function App() {
  const [activeTab, setActiveTab] = useState("text");

  return (
    <div className="container">
      <h1>AI Credibility Engine</h1>

      <div className="tabs">
        <button
          className={activeTab === "text" ? "active" : ""}
          onClick={() => setActiveTab("text")}
        >
          Text Analyzer
        </button>

        <button
          className={activeTab === "image" ? "active" : ""}
          onClick={() => setActiveTab("image")}
        >
          Image Analyzer
        </button>
      </div>

      {activeTab === "text" && <TextAnalyzer />}
      {activeTab === "image" && <ImageUploader />}
    </div>
  );
}
