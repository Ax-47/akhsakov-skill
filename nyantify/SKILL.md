---
name: "nyantify"
description: "Rewrite any text the user gives into cute cat-speak: เนี๊ยน for Thai, nya/nyan for English, plus varied kaomoji. Use on /nyantify or when asked to nyantify, nyan-ify or make text เนี๊ยน."
---

# Nyantify

Turn a piece of text into a cute, cat-flavored version of itself. The user will usually paste the text after the command ("/nyantify พรุ่งนี้ประชุม 10 โมง") or point at something earlier in the chat ("nyantify that"). If there's no text at all, ask for it in one short line.

## How to transform

- **Keep the meaning exactly.** Every fact, number, name, time, link and instruction survives untouched. Nyantifying changes the voice, never the content.
- **Add the cat particle at sentence ends**, at a natural rhythm — most sentences, not every clause:
  - Thai → **เนี๊ยน** ("พรุ่งนี้ประชุม 10 โมงเนี๊ยน")
  - English → **nya / nyan / nya~** ("Meeting is at 10 tomorrow, nya~")
  - Mixed text → match each sentence's language.
- **Light cat-speak touches** are welcome but optional and sparing: น้า / งับ / ง่า in Thai; occasional "na" → "nya" swaps in English ("nyow", "nyice") — at most one or two per short text so it stays readable.
- **Kaomoji, not emoji.** Add one kaomoji for a short text, or roughly one per paragraph for longer text, matched to the mood. Vary them — never repeat the same one within a piece, and don't fall back on the same favorites every time. Some to draw from (and others in the same soft style are fine):
  - happy: ヾ(≧▽≦*)o  ٩(ˊᗜˋ*)و  ₍₍ ◝(●˙꒳˙●)◜ ₎₎  (๑>◡<๑)
  - calm: (︶ω︶)  ( ˘ᵕ˘ )  (◡‿◡✿)
  - sorry/sad: (っ- ‸ – ς)  (ᵕ́‸ᵕ̀)  (╥﹏╥)
  - cat: ₍^ >ヮ<^₎  /ᐠ｡ꞈ｡ᐟ\  ฅ(^◕ᴥ◕^)ฅ  ≽^•⩊•^≼  (=^･ω･^=)
  - determined: (ง •̀_•́)ง  ୧(๑•̀ᴗ•́)૭
- **Keep the structure.** Line breaks, lists, headings and paragraphs stay where they were.
- **Never touch code.** Code blocks, inline code, commands, URLs, file paths and email addresses are copied exactly — no particles or kaomoji inside them.
- **Serious content** (apology, bad news, condolences): use a soft เนี๊ยน/nya and at most one gentle kaomoji, no jokes.

## Output

Return the nyantified text on its own, ready to copy — in a plain block if it's more than a line or two — with at most one short line around it. Don't explain what was changed unless asked.

## Examples

Input: /nyantify พรุ่งนี้ประชุม 10 โมง อย่าลืมเอาโน้ตบุ๊คมาด้วย
Output: พรุ่งนี้ประชุม 10 โมงเนี๊ยน อย่าลืมเอาโน้ตบุ๊คมาด้วยน้า ₍^ >ヮ<^₎

Input: nyantify: Sorry I'm late, the train was delayed. I'll be there in 15 minutes.
Output: Sorry I'm late, nya... the train was delayed (ᵕ́‸ᵕ̀) I'll be there in 15 minutes, nyan~

Input: /nyantify Run `cargo test` before you push. Thanks!
Output: Run `cargo test` before you push, nya~ Thanks nyan! ୧(๑•̀ᴗ•́)૭
