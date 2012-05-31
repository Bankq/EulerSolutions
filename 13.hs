-- file:13.hs
-- Euler Prject: Problem 13
main = do fileContent <- (readFile "p13.log")
          xs <-  (map read . lines) fileContent
          print xs