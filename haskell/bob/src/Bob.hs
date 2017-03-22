module Bob (responseFor) where
import Data.Char

cleanChars :: String -> String
cleanChars = filter (not . (`elem` "\t\n\r "))

getLetters :: String -> String
getLetters = filter isLetter

strIsUpper :: String -> Bool
strIsUpper str
  | upperStr = True
  | otherwise = False
  where
    upperStr = all (==True) boolUpperStr
    boolUpperStr = map isUpper str

strHasChars :: String -> Bool
strHasChars str
  | gotChars = True
  | otherwise = False
  where
    gotChars = True `elem` map isLetter str

responseFor :: String -> String
responseFor str
  | cleanStr == "" = "Fine. Be that way!"
  | hasChars && upperStr = "Whoa, chill out!"
  | last cleanStr == '?' = "Sure."
  | otherwise = "Whatever."
  where
    cleanStr = cleanChars str
    letters = getLetters cleanStr
    hasChars = strHasChars letters
    upperStr = strIsUpper letters


