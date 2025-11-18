import React, { Fragment } from "react";
import Logo from "./logo";
import { Link } from "react-router-dom";
const Footer = () => {
  const SocialIcons = [
    {
      alt: "facebook",
      url: "https://cdn-icons-png.flaticon.com/128/5968/5968764.png",
    },
    {
      alt: "instagram",
      url: "https://cdn-icons-png.flaticon.com/128/4138/4138124.png",
    },
    {
      alt: "Youtube",
      url: "https://cdn-icons-png.flaticon.com/128/4494/4494485.png",
    },
    {
      alt: "Pinterest",
      url: "https://cdn-icons-png.flaticon.com/128/145/145808.png",
    },
  ];
  return (
    <div className="flex justify-start mb-0 m-3 p-3 shadow-2xl shadow-black w-full mx-0 select-none">
      <div className="w-[40%] m-5">
        <div className="m-auto  ml-5">
          <Logo />
          <p className="text-wrap text-justify left-0 pt-1 select-none">
            {" "}
            A platform where users upload and share images publicly, edit
            details anytime, and manage secure accounts with JWT.
          </p>
        </div>
      </div>

      <div className="flex flex-col my-auto m-auto w-[40%]">
        <p className="p-2 pb-0.5 text-center font-medium">
          join us on Social media
        </p>

        <div className="flex flex-row justify-center">
          {SocialIcons.map((data) => {
            return (
              <li
                key={data.alt}
                className="list-none cursor-pointer select-none p-2 "
              >
                <img src={data.url} alt="data.alt" className="h-[40px] m-2" />
              </li>
            );
          })}
        </div>
        <p className="p-2 pt-0 text-center font-extralight">
          Copyright resevered © Satyam Yadav 2025
        </p>
      </div>

      <div className="flex flex-col justify-start text-left m-5 w-[20%] p-2 ml-auto">
        {["Feedback", "Developer", "Contact"].map((text) => {
          return (
            <Fragment key={text}>
              <Link to={"/" + text.toLowerCase()}>
                <li
                  key={text}
                  className="list-none cursor-pointer p-2 rounded-sm font-semibold hover:bg-gray-300"
                >
                  {text}
                </li>
              </Link>
            </Fragment>
          );
        })}
      </div>
    </div>
  );
};

export default Footer;
