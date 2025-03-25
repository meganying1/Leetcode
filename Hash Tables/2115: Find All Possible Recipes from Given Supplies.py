# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies
# difficulty: medium
# topics: array, hash table, string, graph, topological sort

# problem:
# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
# Return a list of all the recipes that you can create. You may return the answer in any order.
# Note that two recipes may contain each other in their ingredients.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipesIndex = {recipes[i]:i for i in range(len(recipes))}
        canMake = {supply:True for supply in supplies}
        
        def checkRecipe(recipe, visited):
            if recipe in canMake: return canMake[recipe]
            if recipe in visited or recipe not in recipesIndex: return False
            visited.add(recipe)
            canMake[recipe] = all(checkRecipe(ingredient, visited) for ingredient in ingredients[recipesIndex[recipe]])
            return canMake[recipe]
        
        return [recipe for recipe in recipes if checkRecipe(recipe, set())]
# time complexity: O(n+m+s), where n is the number of recipes, m is the number of ingredients across all recipes, and s is the number of supplies
#   processing recipesDict and suppliesSet take O(n) and O(s) time respectively
#   we memoize results, so across all DFS calls, we only process each recipe and ingredient once
# space complexity: O(n+m)
#   visited, recipesDict, and recursion stack take up O(n) space
#   canMake takes up O(n+m) space

'''
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipesDict = {recipes[i]:i for i in range(len(recipes))}
        suppliesSet = set(supplies)
        cache = {}
        res = []
        n = len(recipes)
        visited = [False] * n
        
        def canMake(i):
            if i in cache: return cache[i]
            if visited[i]: return False
            visited[i] = True
            for ingredient in ingredients[i]:
                if ingredient not in suppliesSet and ingredient not in recipesDict:
                    cache[i] = False
                    visited[i] = False
                    return False
                elif ingredient in recipesDict:
                    if not canMake(recipesDict[ingredient]):
                        cache[i] = False
                        visited[i] = False
                        return False
            cache[i] = True
            res.append(recipes[i])
            visited[i] = False
            return True
            
        for i in range(n):
            canMake(i)
        return res
'''
