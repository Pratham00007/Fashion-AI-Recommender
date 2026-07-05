
import { useState } from "react";
import api from "../services/api";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState("");
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    const selected = e.target.files[0];

    setFile(selected);

    if (selected) {
      setPreview(URL.createObjectURL(selected));
    }
  };

  const uploadImage = async () => {
    if (!file) {
      alert("Select Image");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await api.post("/upload", formData);

    setResult(response.data);
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "20px",
        marginTop: "40px",
      }}
    >
      <input type="file" accept="image/*" onChange={handleChange} />

      {preview && <img src={preview} alt="" width="250" />}

      <button onClick={uploadImage}>Analyze Image</button>

      {result && (
        <div
          style={{
            marginTop: 20,
            border: "1px solid gray",
            padding: 20,
            borderRadius: 10,
            width: 350,
          }}
        >
          <h3>Analysis</h3>

          <p>
            <b>Face :</b>
            {result.faceDetected ? " Yes" : " No"}
          </p>

          <p>
            <b>Body :</b>
            {result.bodyDetected ? " Yes" : " No"}
          </p>

          <p>
            <b>Pose Landmarks :</b>
            {result.bodyLandmarks}
          </p>

          <p>
            <b>Body Shape :</b>
            {result.bodyShape}
          </p>

          {result.measurements && (
            <>
              <hr />

              <h3>Measurements</h3>

              <p>
                <b>Height :</b>
                {result.measurements.height}
              </p>

              <p>
                <b>Shoulder :</b>
                {result.measurements.shoulderWidth}
              </p>

              <p>
                <b>Waist :</b>
                {result.measurements.waistWidth}
              </p>

              <p>
                <b>Hip :</b>
                {result.measurements.hipWidth}
              </p>
            </>
          )}
        </div>
      )}

      {result?.recommendations && (
        <div
          style={{
            marginTop: 40,
            width: "100%",
            maxWidth: 1000,
          }}
        >
          <h2>Recommended Clothes</h2>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
              gap: 20,
            }}
          >
            {result.recommendations.map((item, index) => (
              <div
                key={index}
                style={{
                  border: "1px solid #ddd",
                  borderRadius: 10,
                  padding: 10,
                  textAlign: "center",
                }}
              >
                <img
                  src={item.image}
                  alt={item.name}
                  style={{
                    width: "100%",
                    height: 250,
                    objectFit: "cover",
                    borderRadius: 8,
                  }}
                />

                <h4>{item.name}</h4>

                <p>
                  <b>Category:</b> {item.category}
                </p>

                <p>
                  <b>Color:</b> {item.color}
                </p>

                <p>
                  <b>Season:</b> {item.season}
                </p>

                <p>
                  <b>Usage:</b> {item.usage}
                </p>

                <p>
                  <b>Score:</b> {item.score}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadBox;

