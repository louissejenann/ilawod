# ILAWOD

> *"There is a place where the sea does not end and the land does not begin."*

**ILAWOD** is a narrative visual novel set in the fictional Filipino coastal village of **Panhuy-an** — a community built on stilts above tidal water, where the sea feeds the people and the people know never to take more than they are given.

When a trip into the mangrove goes wrong, you and your dog Kadyos are pulled into the spirit realm beneath the roots. To find your way home, you must help the spirits of the bakawan revive their fading festival — before the transformation consuming you both is complete.

---

## Story

You are **Kilaw**, a young villager who wanders too close to the bakawan after dark.

What begins as an accident becomes a three-moon journey through a world woven from old stories. To appease the **Bakunawa** — a great sea serpent threatening to swallow the moon — you must help the spirits prepare their ancient festival: the food, the costumes, the dance, the music, the offerings.

The festival must be worthy. The clock is the slow creep of scales spreading across your skin.

---

## Features

- **Filipino folklore and coastal culture** — rooted in Visayan traditions, mangrove ecology, and the mythology of the Bakunawa
- **Multiple endings** — a good, neutral, and bad outcome determined by how well you help the spirits across five preparation minigames
- **Score-based narrative** — your choices across food, costume, dance, music, and props accumulate into a final score that shapes the ending
- **A cast of spirit characters** — Ba-O, Sigay, Lusay, Sili-Sili, Bilong-Bilong, Kasag, and others, each with their own domain and personality
- **Kadyos** — your dog, who is in this with you, all the way to the fins

---

## Characters

| Character | Role |
|---|---|
| **Kilaw** | The player character. A villager who wandered too far. |
| **Kadyos** | Kilaw's dog. Loyal, perceptive, gradually becoming more fish than dog. |
| **Ba-O** | An elder spirit of the bakawan. Warm, watchful, and unhurried. |
| **Dawa** | A fisherwoman by the water's edge. Knows more than she lets on. |
| **Sigay** | A spirit with an eye for beauty and light. |
| **Lusay** | Tends the lanterns — sometimes wrong, always sincere. |
| **Sili-Sili** | Spirited and particular about her domain. |
| **Bilong-Bilong** | Quiet and deliberate. |
| **Kasag** | Oversees the music. Patient, but exacting. |
| **Toto** | A spirit of the festival grounds. |

---

## Endings

Your final score across the five festival preparations determines the outcome:

- **Good Ending** — The Bakunawa is satisfied. The moon is spared. You go home.
- **Neutral Ending** — The festival buys time, but nothing more. A choice remains: stay, or leave changed.
- **Bad Ending** — The festival fails. The moon is swallowed. The village lights lanterns for you every night after.

---

## Built With

- [Ren'Py](https://www.renpy.org/) — Visual Novel Engine
- Custom UI and styling via `screens.rpy` and `style.rpy`
- Original assets: backgrounds, character art, music, and fonts

---

## Setup & Running

1. Download and install [Ren'Py](https://www.renpy.org/latest.html)
2. Clone this repository:
```bash
   git clone https://github.com/louissejenann/ilawod.git
```
3. Install [Git LFS](https://git-lfs.github.com) and run:
```bash
   git lfs install
   git lfs pull
```
4. Move the cloned folder into your Ren'Py **projects directory**
   - You can find or change this path in the launcher under **Preferences → Projects Directory**
5. Open the Ren'Py launcher — the project will appear automatically
6. Select **ILAWOD** and click **Launch Project**

---

## Development

```
ilawod/
├── game/
│   ├── script.rpy       # Main narrative script
│   ├── options.rpy      # Game configuration
│   ├── screens.rpy      # UI screens
│   ├── gui.rpy          # GUI configuration
│   ├── images/          # Backgrounds, character art, and audio
│   ├── fonts/           # Custom typography
│   ├── gui/             # UI assets and icons
│   ├── libs/            # External libraries
│   ├── tl/              # Translations
│   └── minigames/       # Festival minigame scripts
│       ├── food.rpy
│       ├── dance.rpy
│       ├── music.rpy
│       ├── props.rpy
│       ├── costume.rpy
│       └── utils.rpy    # Shared styles and scoring
├── .gitattributes
└── .gitignore
```

---

*The bakawan does not forget. Pay attention — attention, in Panhuy-an, is a kind of offering.*