allPageRequests = [4,7,6,1,7,6,1,2,7,2]
numPageFrames = 3
pageFaults = 0
pageFrames = []

for page in allPageRequests:
    if page not in pageFrames:
        if len(pageFrames) < numPageFrames:
            pageFrames.append(page)
        else:
            pageFrames = pageFrames[1:] + [page]
        pageFaults+=1
        print(f"Page input {page} : page frames - {pageFrames}, fault")
    else:
        print(f"Page input {page} : page frames - {pageFrames}, hit")

print(f"\nPage Faults = {pageFaults}, Page Hits = {len(allPageRequests)-pageFaults}")
            
