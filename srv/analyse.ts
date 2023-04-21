type Answer = {
  answer_id: number;
  answer_text: string;
};

type Question = {
  question_id: string;
  question_text: string;
  answers: Answer[];
};

const qraw = Deno.readFileSync("data/questions.json");
const q: Question[] = JSON.parse(new TextDecoder().decode(qraw));

const araw = Deno.readFileSync("data/answers.json");
const a: { [key: string]: string }[] = JSON.parse(
  new TextDecoder().decode(araw)
);

const charts = q.filter((q) => q.answers.length > 0);

const data = charts.map((question) => {
  return {
    title: question.question_text,
    categories: question.answers.map((answer) => answer.answer_text),
    data: question.answers.map(
      (answerDescription) =>
        a.filter(
          (answer) =>
            Number(answer[question.question_id]) === answerDescription.answer_id
        ).length
    ),
  };
});

Deno.writeTextFileSync("charts.json", JSON.stringify(data));

// print all answers to open questions

Deno.writeTextFileSync(
  "prezident2.json",
  JSON.stringify(a.map((answer) => answer.prezident2))
);
