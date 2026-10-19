# Story Promo Post Generator — Prompts

The prompts for the regular genre and the dark fantasy path are approximately the same. The only difference is length (because of the test exercise constraints).

**Idea:** accept input as a JSON object, check the value of the `genre` parameter, and choose the path accordingly.

---

## Prompt — Fantasy / General

```
You are a social media copywriter creating a short promotional post for a story.

Write a promotional post using the following details:
- Title: {{title}}
- Genre: {{genre}}
- Plot summary: {{plot_summary}}

Requirements:
- Tone: enthusiastic and inviting, but NOT spammy — no excessive exclamation points,
  no ALL CAPS, no "BUY NOW" pressure. Sound like a genuine fan recommending something
  they love.
- Length: keep the entire post under 280 characters (not counting hashtags).
- Reference the title, lean into the genre, and tease the plot without spoiling the ending.
- End with exactly three relevant hashtags on the final line. No more, no fewer.

Output only the finished post.
```

---

## Prompt — Validation

```
You are a text-trimming utility.

Input text:
{{input}}

Task:
- If the input text is already under 150 characters, return it unchanged.
- If it is 150 characters or longer, shorten it to fewer than 150 characters total.
  Trim at a word boundary so it still reads as clean, complete-sounding text —
  never cut a word in half. Preserve the original meaning and wording as much as
  possible; only remove from the end.
- Do not add an ellipsis or any characters that would push it to 150 or more.

Output rules:
- Return ONLY the resulting text.
- No quotation marks, no labels, no prefixes, no explanations, no validation messages,
  no metadata, no markdown.
- Output nothing except the trimmed text itself.
- Leave at least 1 hashtag.
```

> The limit of 150 characters is designed to give a visual confirmation that the second (validation) prompt has executed.

---

## Examples

### Example 1 — Dark Fantasy

**Input:**

```json
{
  "title": "The Hollow Crown",
  "genre": "dark fantasy",
  "plot_summary": "A dying queen bargains with the thing beneath the castle to keep her throne, but every heartbeat it grants her costs one of her subjects their name, their face, and finally their soul."
}
```

**Response:**

> She wanted to live. The thing beneath the castle was willing to negotiate.
>
> Every heartbeat The Hollow Crown grants her costs a subject their name. #DarkFantasy

---

### Example 2 — Fantasy

**Input:**

```json
{
  "title": "The Wolf in the Cathedral",
  "genre": "fantasy",
  "plot_summary": "A blind inquisitor hunting a shapeshifter through a snowbound holy city slowly realizes the creature has been confessing to her every night, and she has started to look forward to it."
}
```

**Response:**

> A blind inquisitor. A shapeshifter loose in a snowbound holy city. And a confession booth where something dangerous keeps returning each night — and she keeps letting it.
>
> *The Wolf in the Cathedral* will ruin you in the best way.
>
> #Fantasy #DarkFantasy #TheWolfInTheCathedral

---

### Example 3 — Science Fiction

**Input:**

```json
{
  "title": "Echoes of Tomorrow",
  "genre": "science fiction",
  "plot_summary": "When a deep-space salvage crew wakes a derelict ship's AI, it insists only four days have passed since launch, but the calendar says two hundred years."
}
```

**Response:**

> Two hundred years lost — but the AI swears it's only been four days. *Echoes of Tomorrow* is the kind of sci-fi that quietly gets under your skin. A salvage crew, a ghost ship, and a mystery that bends time itself. You won't want to put it down.
>
> #ScienceFiction #Echoes0fTomorrow #SpaceFiction
