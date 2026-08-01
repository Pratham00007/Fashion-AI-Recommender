import "../styles/theme.css";
import Header from "../components/Header";
import UploadBox from "../components/UploadBox";

function Home() {
  return (
    <div className="app-shell">
      <Header />
      <UploadBox />
    </div>
  );
}

export default Home;
