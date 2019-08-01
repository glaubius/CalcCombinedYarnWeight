# Calculate weight of two yarns combined

length_100g <- data.frame("Standard Weight"=c("7 - Jumbo, Roving", 
                                              "6 - Super Bulky",
                                              "5- Bulky, Chunky, 14 ply",
                                              "4 - Medium, Worsted, Aran, 10/12 ply",
                                              "3 - Light, DK, Light Worsted, 8 ply",
                                              "2 - Fine, Sport, 4 ply",
                                              "1 - Super Fine, Fingering, 3 ply",
                                              "0 - Lace, Cobweb"), 
                          "Low Length per 100 gr"=c(0, 50, 90, 110, 240, 300, 400, 600))

y1_weight <- 100
y2_weight <- 100

y1_length <- 500
y2_length <- 200

y1_length_unit <- 'm'
y2_length_unit <- 'yd'

if (y1_length_unit == 'm') {
  y1_weight_per_meter <- y1_weight / y1_length
} else {
  y1_weight_per_meter <- y1_weight / (y1_length * 0.9144)
}

if (y2_length_unit == 'm') {
  y2_weight_per_meter <- y2_weight / y2_length
} else {
  y2_weight_per_meter <- y2_weight / (y2_length * 0.9144)
}

combined_weight_per_meter <- y1_weight_per_meter + y2_weight_per_meter

meters_per_100g <- 100 / combined_weight_per_meter

standard_weight <- ""



length_100g$Low.Length.per.100.gr[5]
length_100g$Standard.Weight[5]

standard_weight