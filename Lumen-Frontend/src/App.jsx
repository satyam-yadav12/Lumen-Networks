import { useState } from "react";

import "./App.css";
import Navbar from "./components/Navbar";
import Image from "./components/image";
import Footer from "./components/Footer";
import PageRoutes from "./routes/PageRoutes";

function App() {
  return (
    <>
      <PageRoutes />
    </>
  );
}

export default App;
