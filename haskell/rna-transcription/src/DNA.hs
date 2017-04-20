module DNA (toRNA) where



toRNA :: String -> Maybe String
toRNA xs =
      | c == 'G' = 'C'
      | c == 'T' = 'A'
      | c == 'A' = 'U'
      | c == 'C' = 'G'
      | otherwise = Nothing
      parsed = map parseRNA xs
