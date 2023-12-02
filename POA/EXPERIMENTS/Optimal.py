allPageRequests = [4,7,6,1,7,6,1,2,7,2]
numPageFrames = 3
pageFaults = 0
pageFrames = []

def findPageToReplace(allPageRequests, currentIndex, pageFrames):
    indexToReplace = -1
    futurePages = []

    for page in allPageRequests[-1:currentIndex]:
        if page in pageFrames:
            futurePages.append(page)

    if indexToReplace == -1:
        indexToReplace = 0
    elif len(futurePages) < len(pageFrames):
        unused_pages = [page for page in pageFrames if page not in futurePages]
        indexToReplace = pageFrames.index(unused_pages[0])

    return indexToReplace

for i,page in enumerate(allPageRequests):
    if page not in pageFrames:
        if len(pageFrames) < numPageFrames:
            pageFrames.append(page)
        else:
            indexToReplace = findPageToReplace(allPageRequests, i, pageFrames)
            pageFrames[indexToReplace] = page
        pageFaults+=1
        print(f"Page input {page} : page frames - {pageFrames}, fault")
    else:
        print(f"Page input {page} : page frames - {pageFrames}, hit")

print(f"\nPage Faults = {pageFaults}, Page Hits = {len(allPageRequests)-pageFaults}")
            
