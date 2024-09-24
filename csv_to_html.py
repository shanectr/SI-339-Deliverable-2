import csv

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]

      for row in data[5:-2]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5]
            })

   return {
      "name": athlete_name,
      "season_records": records,
      "race_results": races
   }    

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel = "stylesheet" href = "css/style.css">
      <link rel = "stylesheet" href = "css/reset.css">
      

      <title>{data["name"]}</title>
   </head>
   <body>

   <header>
      <h1>{data["name"]}</h1>
      <!--Athlete would input headshot-->
      <img src="path/athlete_img.jpg" alt="Athlete headshot"> 
   </header>

      <section id= "athlete-sr-table">
         <h2>Athlete's Seasonal Records (SR) per Year</h2>
            <table>
                  <thead>
                     <tr>
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <th>{sr["year"]}</th>
                        <th>{sr["sr"]}</th>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>

                        <h2>Race Results</h2>

                        <section id="athlete-result-table">
                            <label for="sort">Sort race data:</label>

                            <!-- sort data using JavaScript if sort filter is selected
                            this section should filter based on time, date, or place-->
                            <label for="race-data-sort"> Sort races by:</label>
                            <select id="race-data-sort">
                            <option value="time-fastest">Time: Fastest first</option>
                            <option value="time-slowest">Time: Slowest first</option>
                            <option value="date-latest">Date: Latest first</option>
                            <option value="date-earliest">Date: Earliest first</option>
                            <option value="place-highest">Place: Highest first</option>
                            <option value="place-lowest">Place: Lowest first</option>
                            </select>

                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row">
                                    <td>
                                       <a href="Race Link">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
               </body>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)


def main():
   filename1 = "athletes/mens_team/Alex Nemecek18820260.csv"
   filename2 = "athletes/mens_team/Enshu Kuan23687884.csv"

   # read data from file
   athlete_data1 = process_athlete_data(filename1)
   # using data to generate templated athlete page
   gen_athlete_page(athlete_data1, "alex_nemecek.html")

   # read data from file
   athlete_data2 = process_athlete_data(filename2)
   # using data to generate templated athlete page
   gen_athlete_page(athlete_data2, "enshu_kuan.html")

if __name__ == '__main__':
    main()
