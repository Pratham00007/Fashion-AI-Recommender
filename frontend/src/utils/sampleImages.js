/**
 * Auto-loads every sample image inside src/assets/samples/.
 *
 * Vite's import.meta.glob scans the folder at build/dev time, so you
 * NEVER need to edit this file when you add or remove images.
 * Just drop files into src/assets/samples/ named with a leading
 * number, e.g. 1.png, 2.jpg, 3.webp, 4.jpeg ... in any amount,
 * any mix of extensions, and they will show up automatically
 * (sorted by that number).
 *
 * In dev mode (npm run dev) Vite's glob is reactive — adding a new
 * file to the folder triggers an automatic reload, no restart needed.
 */
const modules = import.meta.glob(
  "../assets/samples/*.{png,jpg,jpeg,webp,PNG,JPG,JPEG,WEBP}",
  { eager: true, import: "default" }
);

function extractNumber(path) {
  const match = path.match(/(\d+)(?=\.\w+$)/);
  return match ? parseInt(match[1], 10) : Number.MAX_SAFE_INTEGER;
}

const sampleImages = Object.entries(modules)
  .map(([path, src]) => {
    const name = path.split("/").pop();
    return {
      id: name,
      name,
      src,
      number: extractNumber(path),
    };
  })
  .sort((a, b) => a.number - b.number);

/**
 * Turns a bundled sample image URL back into a real File object so it
 * can be sent through the exact same /upload flow as a user's own
 * upload (FormData + axios), no backend changes required.
 */
export async function sampleToFile(sample) {
  const response = await fetch(sample.src);
  const blob = await response.blob();
  const ext = sample.name.split(".").pop();
  const mime = blob.type || `image/${ext === "jpg" ? "jpeg" : ext}`;
  return new File([blob], sample.name, { type: mime });
}

export default sampleImages;
