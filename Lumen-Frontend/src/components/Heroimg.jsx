import { Button } from "@mui/material";
import React, { useContext, useEffect, useState } from "react";
import TypeText from "./TypeText";
import { ThemeContext } from "../context/Themecontext";

const Heroimg = () => {
  const [tag, setTag] = useState("Discover, search, and share images");

  const { theme: mode, Imgtag } = useContext(ThemeContext);

  const [bgImg, setBgImg] = useState(`/${Imgtag}-image-1.avif`);

  const updateTag = () =>
    setTag(
      tag == "Discover, search, and share images"
        ? "Upload your images for everyone to see"
        : "Discover, search, and share images"
    );

  useEffect(() => {
    const chagneTag = setTimeout(() => {
      updateTag();
    }, 5000);

    return () => clearTimeout(chagneTag);
  }, [tag]);

  useEffect(() => {
    let num = 1;
    console.log(Imgtag);
    const changeBack = setInterval(() => {
      if (num <= 4) {
        setBgImg(`/${Imgtag}-image-${num + 1}.avif`);
        num = num + 1;
      } else {
        num = 1;
        setBgImg(`/${Imgtag}-image-${num}.avif`);
      }
    }, 5000);

    return () => clearInterval(changeBack);
  }, [Imgtag]);

  return (
    <div>
      <div
        className="bg-transparent bg-center bg-clip-border bg-no-repeat bg-cover w-full relative h-[400px] inset-0 bg-gradient-to-b from-black/60 to-transparent"
        style={{ backgroundImage: `url(${bgImg} )` }}
      >
        <div className="absolute w-full h-full flex flex-col items-center justify-center text-centerinset-0 bg-gradient-to-b from-black/40 to-transparent">
          <h1
            className="text-4xl font-bold p-5 m-2 pb-1
       mb-0 text-shadow-2xs text-shadow-white"
          >
            welcome to Lumen Networks!
          </h1>
          <h2 className="font-stretch-normal p-3 m-2 pt-0 mt-0   text-shadow-2xs text-shadow-white h-[40px]">
            <TypeText text={tag} />
          </h2>

          <div className="p-2 m-3 flex justify-center">
            <Button variant="contained" color="primary">
              {" "}
              Login / Register
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Heroimg;
