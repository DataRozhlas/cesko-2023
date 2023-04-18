// mod.ts
import { readCsv } from "./csv_reader.ts";
import { writeAll } from "./deps.ts";

const csvFilePath = "data/odpovedi.csv";

(async () => {
  try {
    const csvData = await readCsv(csvFilePath);
    const csvDataJson = JSON.stringify(csvData, null, 2);
    const file = await Deno.open("../src/assets/answers.json", {
      write: true,
    });
    writeAll(file, new TextEncoder().encode(csvDataJson));
    file.close();
  } catch (error) {
    console.error("Error reading CSV file:", error);
  }
})();
