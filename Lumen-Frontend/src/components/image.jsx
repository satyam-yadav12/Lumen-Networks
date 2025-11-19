import React from "react";
import mock_file from "../assets/users.user_imgs.json";
import mock_images from "../assets/mockData.json";

const Image = () => {
  const images = mock_images;
  // console.log(images);
  return (
    <div className="columns-1 sm:columns-2 lg:columns-3 gap-4 px-4">
      {images.map((data, index) => {
        return (
          <div
            key={index}
            className="break-inside-avoid overflow-hidden rounded-xl my-4 w-[90vw] sm:w-[45vw] lg:w-[30vw]"
          >
            <img
              src={data.url2}
              alt="img"
              loading="lazy"
              className=" object-cover m-auto rounded-xl"
            />
          </div>
        );
      })}
    </div>
  );
};

export default Image;
