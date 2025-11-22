import { Rating, Button } from "@mui/material";
import React from "react";

const Feedback = () => {
  return (
    <div>
      <div>
        {" "}
        <div className="h-15 my-5">
          <Rating name="rating" size="large" defaultValue={0} />
        </div>
        <div className="w-5/6 m-auto grid grid-cols-1 md:grid-cols-2 gap-3">
          <div className="gap-2 m-2 p-2 w-full">
            <label className="block" htmlFor="title">
              Enter Name{" "}
            </label>
            <input
              className="w-full border border-black p-4 my-1 block dark:bg-gray-200 dark:border-white dark:text-black "
              type="text"
              name="title"
              id="title"
            />
          </div>
          <div className="gap-2 m-2 p-2 w-full">
            <label className="block" htmlFor="title">
              Enter Email{" "}
            </label>
            <input
              className="w-full border border-black p-4 my-1 block dark:bg-gray-200 dark:border-white dark:text-black "
              type="text"
              name="email"
              id="email"
            />
          </div>

          <div className="gap-2 m-2 p-2 w-full">
            <label className="block" htmlFor="description">
              Enter Title
            </label>
            <textarea
              name="description"
              id="description"
              className="w-full  h-15  border border-black p-4  my-1 block dark:border-white dark:bg-gray-200 dark:text-black"
            ></textarea>
          </div>
          <div className="gap-2 m-2 p-2 w-full">
            <label className="block" htmlFor="Tag">
              Enter Description
            </label>
            <input
              className="w-full border border-black p-4 my-1 block dark:bg-gray-200 dark:border-white dark:text-black"
              type="text"
              name="tag"
              id="Tag"
            />
          </div>
        </div>
      </div>
      <div className="m-auto my-4 col-span-2">
        <Button variant="contained">Send Feedback</Button>
      </div>
    </div>
  );
};

export default Feedback;
