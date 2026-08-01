import sampleImages from "../utils/sampleImages";

function SampleGallery({ selectedId, onSelect, disabled }) {
  return (
    <div className="contact-sheet reveal reveal-4">
      <div className="contact-sheet__head">
        <span className="contact-sheet__title">Or try a sample photo</span>
        <span className="contact-sheet__count mono">
          {sampleImages.length.toString().padStart(2, "0")} AVAILABLE
        </span>
      </div>

      {sampleImages.length === 0 ? (
        <p className="sample-empty">
          No samples yet — add images to{" "}
          <code>src/assets/samples/</code> (e.g. <code>1.png</code>,{" "}
          <code>2.jpg</code>, <code>3.webp</code>) and they'll appear here
          automatically.
        </p>
      ) : (
        <div className="sample-grid">
          {sampleImages.map((sample, index) => (
            <button
              type="button"
              key={sample.id}
              className={`sample-thumb${
                selectedId === sample.id ? " is-selected" : ""
              }`}
              disabled={disabled}
              onClick={() => onSelect(sample)}
              title={sample.name}
            >
              <img src={sample.src} alt={`Sample ${index + 1}`} loading="lazy" />
              <span className="sample-thumb__num">
                {(index + 1).toString().padStart(2, "0")}
              </span>
              <span className="sample-thumb__check">✓</span>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default SampleGallery;
