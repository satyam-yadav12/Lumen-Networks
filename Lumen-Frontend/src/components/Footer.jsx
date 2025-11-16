import React from "react";

const Footer = () => {
  return (
    <div className="flex justify-evenly mb-0 m-3 p-3">
      {["Feedback", "Developer", "Contact"].map((text) => {
        return (
          <li key={text} className="list-none">
            {text}
          </li>
        );
      })}
    </div>
  );
};

export default Footer;
