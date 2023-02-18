const FetchData = async (keyword) => {
  try {
    let url =
      "https://annasearch.search.windows.net/indexes/abhishek/docs?api-version=2021-04-30-Preview&search=" +
      keyword;
    const response = await fetch(url, {
      method: "Get",
      headers: {
        "api-key": "GdiRFuzhIggWBRBaQPsNqx5Y9mm6LtkIhBhrciV5wwAzSeCfm87M",
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error("Incorrect response recived");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    return "error";
  }
};


module.exports = {
  FetchData,
};
