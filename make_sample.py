import sys

from topic_ideas.core import TopicAssortment

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} output.tsv")
        sys.exit(1)

    output_path = sys.argv[1]

    ta = TopicAssortment()
    ta.load_nouns()
    ta.load_adjectives()
    ta.write_sample(output_path)
    sys.exit(0)

if __name__ == "__main__":
    main()

