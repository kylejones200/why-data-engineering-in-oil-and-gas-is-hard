"""Generated from Jupyter notebook: spacy_ner_geological_text

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import spacy


def main():
    nlp = spacy.load("./output/model-best/")
    with open("bgs-geo-testing-data.txt") as file:
        lines = file.readlines()
        for line in lines:
            doc = nlp(line)
            spacy.displacy.render(doc, style="ent", jupyter=True)


def main() -> None:
    main()


if __name__ == "__main__":
    main()
