import { useRef, useState } from "react";
import api from "../services/api";
import SampleGallery from "./SampleGallery";
import { sampleToFile } from "../utils/sampleImages";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [isDragging, setIsDragging] = useState(false);
  const [selectedSampleId, setSelectedSampleId] = useState(null);
  const inputRef = useRef(null);

  const applyFile = (selected) => {
    if (!selected) return;
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
    setResult(null);
    setError("");
  };

  const handleChange = (e) => {
    setSelectedSampleId(null);
    applyFile(e.target.files[0]);
  };

  const handleSampleSelect = async (sample) => {
    try {
      setError("");
      setSelectedSampleId(sample.id);
      const asFile = await sampleToFile(sample);
      applyFile(asFile);
    } catch {
      setError("Couldn't load that sample image. Try another one.");
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    setSelectedSampleId(null);
    const dropped = e.dataTransfer.files?.[0];
    if (dropped) applyFile(dropped);
  };

  const uploadImage = async () => {
    if (!file) {
      setError("Select or drop a photo first.");
      return;
    }
    setLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", file);
      const response = await api.post("/upload", formData);
      setResult(response.data);
    } catch {
      setError("Analysis failed. Check that the backend is running and try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-content">
      <div className="dropzone-wrap reveal reveal-2">
        <div
          className={`dropzone${isDragging ? " is-dragging" : ""}`}
          onClick={() => inputRef.current?.click()}
          onDragOver={(e) => {
            e.preventDefault();
            setIsDragging(true);
          }}
          onDragLeave={() => setIsDragging(false)}
          onDrop={handleDrop}
        >
          <span className="dropzone__tag mono">No. 001 — SUBJECT</span>

          <input
            ref={inputRef}
            className="hidden-input"
            type="file"
            accept="image/*"
            onChange={handleChange}
          />

          {preview ? (
            <div className="preview-frame">
              <img src={preview} alt="Selected preview" />
              <div className="preview-frame__badge mono">
                {selectedSampleId ? `SAMPLE · ${selectedSampleId}` : "READY TO ANALYZE"}
              </div>
            </div>
          ) : (
            <>
              <div className="dropzone__icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                  <path
                    d="M12 16V4M12 4l-4 4M12 4l4 4M4 16v3a2 2 0 002 2h12a2 2 0 002-2v-3"
                    stroke="currentColor"
                    strokeWidth="1.8"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
              </div>
              <div className="dropzone__label">Drop a full-body photo here</div>
              <div className="dropzone__hint">
                or <b>click to browse</b> — JPG, PNG or WEBP
              </div>
            </>
          )}
        </div>
      </div>

      <div style={{ display: "flex", justifyContent: "center", marginTop: 22 }} className="reveal reveal-3">
        <button
          className={`btn btn-primary${loading ? " is-loading" : ""}`}
          onClick={uploadImage}
          disabled={loading}
        >
          {loading ? "Analyzing" : "Analyze Photo"}
          {loading && <span className="spinner" />}
        </button>
      </div>

      {error && (
        <div className="status-banner reveal" style={{ marginTop: 16, textAlign: "center" }}>
          {error}
        </div>
      )}

      <div className="divider-row reveal reveal-3">choose from samples instead</div>

      <SampleGallery
        selectedId={selectedSampleId}
        onSelect={handleSampleSelect}
        disabled={loading}
      />

      {result && (
        <div className="ticket reveal" style={{ marginTop: 34 }}>
          <div className="ticket__head">
            <span className="ticket__title">Body Analysis</span>
            <span className="ticket__stamp">✓ processed</span>
          </div>

          <div className="ticket__grid">
            <div className="ticket__row">
              <b>Face detected</b>
              <span>{result.faceDetected ? "YES" : "NO"}</span>
            </div>
            <div className="ticket__row">
              <b>Body detected</b>
              <span>{result.bodyDetected ? "YES" : "NO"}</span>
            </div>
            <div className="ticket__row">
              <b>Pose landmarks</b>
              <span>{result.bodyLandmarks}</span>
            </div>
            <div className="ticket__row">
              <b>Body shape</b>
              <span>{result.bodyShape}</span>
            </div>
          </div>

          {result.measurements && (
            <>
              <hr className="ticket__divider" />
              <div className="ticket__title" style={{ marginBottom: 14 }}>
                Measurements
              </div>
              <div className="ticket__grid">
                <div className="ticket__row">
                  <b>Height</b>
                  <span>{result.measurements.height}</span>
                </div>
                <div className="ticket__row">
                  <b>Shoulder</b>
                  <span>{result.measurements.shoulderWidth}</span>
                </div>
                <div className="ticket__row">
                  <b>Waist</b>
                  <span>{result.measurements.waistWidth}</span>
                </div>
                <div className="ticket__row">
                  <b>Hip</b>
                  <span>{result.measurements.hipWidth}</span>
                </div>
              </div>
            </>
          )}
        </div>
      )}

      {result?.recommendations && (
        <div className="rec-section reveal" style={{ marginTop: 48 }}>
          <h2 className="rec-section__title">Recommended For You</h2>
          <p className="rec-section__sub">
            Picked to suit your body profile, not what you're already wearing.
          </p>

          <div className="rec-grid">
            {result.recommendations.map((item, index) => (
              <div className="rec-card" key={index}>
                <div className="rec-card__img-wrap">
                  <img src={item.image} alt={item.name} loading="lazy" />
                </div>
                <div className="rec-card__body">
                  <div className="rec-card__name">{item.name}</div>
                  <div className="rec-card__meta">
                    <span className="chip plum">{item.category}</span>
                    <span className="chip">{item.color}</span>
                    <span className="chip gold">{item.season}</span>
                    <span className="chip">{item.usage}</span>
                  </div>
                  <div className="rec-card__score">
                    <span>{item.score}</span>
                    <span className="score-bar">
                      <span
                        className="score-bar__fill"
                        style={{ width: `${Math.min(100, item.score / 2)}%` }}
                      />
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadBox;
