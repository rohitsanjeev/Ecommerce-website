"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("/api/apple-data")
      .then((res) => res.json())
      .then((data) => {
        if (data.products) {
          setProducts(data.products);
        }
      })
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6">Apple Products</h1>
      {products.length > 0 ? (
        <ul className="space-y-4">
          {products.map((product, index) => (
            <li key={index} className="text-lg bg-gray-100 p-4 rounded-lg shadow-md">
              {product}
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading products...</p>
      )}
    </main>
  );
}



