import React, { Suspense } from "react";
// import Image from "../components/image";
import Heroimg from "../components/Heroimg";

const Image = React.lazy(() => import("../components/image"));

const Home = () => {
  return (
    <div>
      <div>
        <Heroimg />
      </div>
      <div className="mt-5">
        <Suspense fallback={<div>Loading...</div>}>
          <Image />
        </Suspense>
      </div>
    </div>
  );
};

export default Home;
