import sys

from topic_ideas.core import TopicAssortment

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.tsv output.html")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    ta = TopicAssortment()
    ta.read_sample(input_path)
    ta.write_html(output_path)
    sys.exit(0)

if __name__ == "__main__":
    main()

