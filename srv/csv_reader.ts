// csv_reader.ts
import { dsvFormat } from "./deps.ts";

interface CsvRow {
  [key: string]: string;
}

const ssv = dsvFormat(";");

// deno-lint-ignore no-explicit-any
export async function readCsv(filePath: string): Promise<any> {
  const fileContent = await Deno.readTextFile(filePath);
  const parsedData = ssv.parse(fileContent);

  return parsedData;
}
