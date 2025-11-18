import React from "react";
import mock_file from "../assets/users.user_imgs.json";

const Image = () => {
  const images = mock_file;
  console.log(images);
  return (
    <div className="columns-3 gap-2">
      {images.map((data) => {
        // console.log(data.secure_url, "data");
        return (
          <li key={data.img_id} className="list-none  p-2">
            <img src={data.secure_url} alt="img" />
          </li>
        );
      })}
    </div>
  );
};

export default Image;
