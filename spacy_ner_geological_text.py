"""Generated from Jupyter notebook: spacy_ner_geological_text

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

import spacy


def main():
    # --- code cell ---

    nlp = spacy.load("./output/model-best/")


    # --- code cell ---

    with open("bgs-geo-testing-data.txt") as file:
        lines = file.readlines()
        for line in lines:
            doc = nlp(line)
            spacy.displacy.render(doc, style="ent", jupyter=True)


if __name__ == "__main__":
    main()
