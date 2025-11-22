import React, { useState } from "react";
import mock_file from "../assets/users.user_imgs.json";
import mock_images from "../assets/photos.json";
import ShowImage from "./ShowImage";
import BasicMenu from "./DropDown";
import MobileMenu from "./MobileMenu";
import { Skeleton } from "@mui/material";

const Image = ({ images = mock_images }) => {
  const [like, setLike] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [show, setShow] = useState(false);
  const [showUri, setShowUri] = useState("");

  const handleLike = (id) => {
    if (like.includes(id)) {
      setLike((prev) => {
        let newArr = prev.filter((val) => val != id);
        return newArr;
      });
    } else {
      setLike((prev) => [...prev, id]);
    }
  };
  // const images = mock_images;
  // console.log(images);
  return (
    <div className="columns-1 sm:columns-2 lg:columns-3 gap-4 px-4">
      <div>
        <ShowImage id={showUri} show={show} setShow={setShow} />
      </div>
      {images.map((data, index) => {
        return (
          <div
            key={index}
            className="group hover:opacity-98 relative break-inside-avoid overflow-hidden rounded-xl my-4 w-[90vw] sm:w-[45vw] lg:w-[30vw]"
          >
            <img
              src={data.photo_image_url}
              alt="img"
              id={data.photo_id}
              loading="lazy"
              className={` object-cover m-auto rounded-xl w-full transition-opacity duration-500 ${
                loaded ? "opacity-100" : "opacity-0"
              } aspect-[${data.photo_width}/${data.photo_height}]`}
              onClick={() => {
                setShow(true);
                setShowUri(data.photo_id);
              }}
              // aspectRatio={`${data.photo_width}/${data.photo_height}`}
              onLoad={() => setLoaded(true)}
            />

            <div
              className={`w-full h-full animate-pulse bg-linear-to-r from-gray-400 via-gray-500 to-gray-400 border-gray-500 rounded-3xl aspect-[${
                data.photo_width
              }/${data.photo_height}]${loaded ? `opacity-0 ` : "opacity-100"} `}
            ></div>
            <div
              onClick={() => {
                setShow(true);
                setShowUri(data.photo_id);
              }}
              className=" hidden  md:flex md:flex-col justify-evenly w-full h-full p-2 text-2xl text-bold text-white font-bold shadow-lg rounded-2xl shadow-black opacity-0 inset-0 group-hover:opacity-100 transition-opacity ease duration-300 text-center top-[50%] left-[50%] transform -translate-x-1/2 -translate-y-1/2 absolute "
            >
              <div className="flex flex-row h-[20%] p-2 mb-auto">
                <img
                  src="/logo.png"
                  alt="logo"
                  className="h-6 w-max object-contain px-2 p-0 mt-2 mr-auto "
                />
                <BasicMenu />
              </div>
              <div className="w-full h-[60%] flex flex-col justify-center items-center">
                <button className="bg-transparent border border-transparent shadow-2xl rounded-3xl opacity-50 p-2 h-max w-max ">
                  Open
                </button>
              </div>
              <div className="flex flex-row h-[20%] p-2 ">
                <p className="h-full w-max  px-2 mr-auto">
                  {data.photographer_username}
                </p>

                {like.includes(`${data.photo_id}`) ? (
                  <img
                    src="https://img.icons8.com/?size=64&id=aId5rVASLwDE&format=png"
                    alt="like"
                    className="ml-auto px-2 mt-2 h-6 invert  object-contain  w-max "
                    onClick={(e) => {
                      e.stopPropagation();
                      e.preventDefault();
                      handleLike(data.photo_id);
                    }}
                  />
                ) : (
                  <img
                    src="https://cdn-icons-png.flaticon.com/128/25/25424.png"
                    alt="like"
                    className="ml-auto px-2 mt-2 h-6 invert  object-contain  w-max "
                    onClick={(e) => {
                      e.stopPropagation();
                      e.preventDefault();
                      handleLike(data.photo_id);
                    }}
                  />
                )}
              </div>
            </div>
            <div className="h-12 p-2 block lg:hidden rounded-2xl">
              <div className="flex flex-row   ">
                <p className="h-full w-max  px-1 pt-1.5 mr-auto font-semibold">
                  {data.photographer_username}
                </p>
                <div className="ml-auto flex flex-row">
                  {like.includes(`${data.photo_id}`) ? (
                    <img
                      src="https://img.icons8.com/?size=64&id=aId5rVASLwDE&format=png"
                      alt="like"
                      className=" px-2 h-7 mt-0.5  object-contain  w-max dark:invert"
                      onClick={(e) => {
                        e.stopPropagation();
                        e.preventDefault();
                        handleLike(data.photo_id);
                      }}
                    />
                  ) : (
                    <img
                      src="https://cdn-icons-png.flaticon.com/128/25/25424.png"
                      alt="like"
                      className=" px-2 h-6  mt-1.5 object-contain  w-max dark:invert"
                      onClick={(e) => {
                        e.stopPropagation();
                        e.preventDefault();
                        handleLike(data.photo_id);
                      }}
                    />
                  )}
                  <MobileMenu />
                </div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default Image;
