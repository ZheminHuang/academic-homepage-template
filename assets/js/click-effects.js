(() => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const symbols = ["∇V", "π", "λ", "u*", "○"];
  let symbolIndex = 0;

  document.addEventListener("pointerdown", (event) => {
    if (reducedMotion.matches || event.button !== 0) {
      return;
    }

    const effect = document.createElement("span");
    effect.className = "click-effect-symbol";
    effect.textContent = symbols[symbolIndex % symbols.length];
    effect.style.left = `${event.clientX}px`;
    effect.style.top = `${event.clientY}px`;
    symbolIndex += 1;

    document.body.appendChild(effect);
    window.setTimeout(() => effect.remove(), 700);
  });
})();
