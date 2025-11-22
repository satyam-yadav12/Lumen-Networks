import React, { useEffect, useState } from "react";
import mockData from "../assets/photos.json";

const ShowImage = ({ id, show, setShow }) => {
  const [imgUrl, setImgUrl] = useState(
    "https://images.unsplash.com/reserve/dRA4UuMBR2K5pxchYcxA_IMG_6965.JPG"
  );
  const [imageDetails, setImageDetails] = useState({
    author: "",
    title: "",
    description: "",
  });

  useEffect(() => {
    let uri = mockData.filter((val) => val.photo_id == id);

    uri.length > 0 && setImgUrl(uri[0].photo_image_url);
    uri.length > 0 &&
      setImageDetails({
        author: uri[0].photographer_username,
        title: uri[0].ai_description,
        description: uri[0].photo_description,
      });
  }, [id]);

  return (
    <>
      {show && (
        // backdrop: full screen, click closes
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 no-scrollbar"
          onClick={() => setShow(false)}
        >
          {/* popup box: stops backdrop click, sized to 5/6 of viewport but clamped with max-h */}
          <div
            className="relativew-full md:w-[90%]  h-[90%] max-h-[90vh] bg-white rounded-2xl shadow-xl overflow-y-auto p-4"
            onClick={(e) => e.stopPropagation()}
          >
            {/* close button top-right */}
            <button
              className=" fixed top-1.5 right-20 text-4xl font-bold"
              onClick={() => setShow(false)}
            >
              ×
            </button>

            {/* content */}
            <div className="flex flex-col items-center justify-start gap-4 pt-6">
              <img
                src={imgUrl}
                alt="main img"
                className="w-3/4 md:h-[50%] max-h-[50%] object-contain"
              />
              <p>{id}</p>

              <div className="w-full text-justify">
                <p className="p-2 font-mono font-semibold">
                  {imageDetails.author}
                </p>
                <p className="p-2 font-mono font-medium">
                  {imageDetails.title}
                </p>
                <p className="p-2 font-mono font-medium">
                  {imageDetails.description}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default ShowImage;
