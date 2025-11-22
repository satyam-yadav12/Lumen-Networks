import React, { Suspense } from "react";
// import Image from "../components/image";
import Heroimg from "../components/Heroimg";
import FilterChips from "../components/FilterChips";
import ImageFallback from "../components/ImageFallback";
import { CircularProgress } from "@mui/material";

const Image = React.lazy(() => import("../components/image"));

const Home = () => {
  return (
    <div>
      <div>
        <Heroimg />
      </div>
      <div>
        <FilterChips />
      </div>
      <div className="mt-5">
        <Suspense fallback={<CircularProgress size={40} />}>
          <Image />
        </Suspense>
      </div>
    </div>
  );
};

export default Home;
