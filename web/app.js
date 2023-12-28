const wordInput = document.querySelector("#input");
const button = document.querySelector("#search");
const loading = document.querySelector("#loading");
const categories = document.querySelector("#categories")
const chat = document.querySelector("#chat")

button.addEventListener("click", async (e) => {
  const word = wordInput.value.trim();

  if (word === "") return;

  loading.innerText = "Loading...";
  const response = await eel.scrape_word(word)();
  loading.innerText = "";

  chat.innerText = response.chat_reply
  categories.innerText = response.categories.join(" - ")
});
