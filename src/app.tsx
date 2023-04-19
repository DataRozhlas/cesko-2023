import { Stack, Heading } from "@chakra-ui/react";
import Highcharts from "highcharts";
import {
  HighchartsProvider,
  HighchartsChart,
  Chart,
  Legend,
  Tooltip,
  XAxis,
  YAxis,
  BarSeries,
} from "react-jsx-highcharts";
import data from "./assets/charts.json";

const plotOptions = {
  bar: {
    pointWidth: 25,
  },
};

export function App() {
  return (
    <HighchartsProvider Highcharts={Highcharts}>
      <Stack>
        {data.map((chart) => (
          <Stack pb={10}>
            <Heading fontSize={"lg"}>{chart.title}</Heading>
            <HighchartsChart plotOptions={plotOptions}>
              <Chart
                type="bar"
                height={chart.categories.length * 50 + 25}
                marginLeft={120}
              />
              <Tooltip shared />
              <XAxis type="category" categories={chart.categories} />
              <YAxis max={100}>
                <BarSeries
                  data={chart.data.map((number) => (number / 7751) * 100)}
                  name={"odpovědi"}
                  dataLabels={{
                    enabled: true,
                    format: "{point.y:.1f} %",
                  }}
                />
              </YAxis>
            </HighchartsChart>
          </Stack>
        ))}
      </Stack>{" "}
    </HighchartsProvider>
  );
}
