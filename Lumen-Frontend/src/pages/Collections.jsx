import React from "react";
import Image from "../components/image";
import mockData from "../assets/photos.json";

const Collections = () => {
  return (
    <div>
      <div className="pt-5 w-[98%] m-auto">
        <Image images={mockData} />
      </div>
    </div>
  );
};

export default Collections;
