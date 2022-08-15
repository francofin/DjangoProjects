import React from "react";
import Link from 'next/link'
import Image from "next/image";

const Footer = () => {
  return (
    <footer className="py-1">
      <p className="text-center mt-1">
        Jobbee - 2021-2022, All Rights Reserved
        <Link
          href="https://storyset.com/people"
          passHref
        >
            <a className="ml-4"
          rel="noreferrer"
          target="_blank">
            People illustrations by Storyset
            </a>
          
        </Link>
      </p>
    </footer>
  );
};

export default Footer;