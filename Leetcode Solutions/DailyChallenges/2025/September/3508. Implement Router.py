# problem link: https://leetcode.com/problems/implement-router/


# Description:
"""
Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

source: A unique identifier for the machine that generated the packet.
destination: A unique identifier for the target machine.
timestamp: The time at which the packet arrived at the router.
Implement the Router class:

Router(int memoryLimit): Initializes the Router object with a fixed memory limit.

memoryLimit is the maximum number of packets the router can store at any given time.
If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.

A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.

Remove the packet from storage.
Return the packet as an array [source, destination, timestamp].
If there are no packets to forward, return an empty array.
int getCount(int destination, int startTime, int endTime):

Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
Note that queries for addPacket will be made in increasing order of timestamp.

 

Example 1:

Input:
["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

Output:
[null, true, true, false, true, true, [2, 5, 90], true, 1]

Explanation

Router router = new Router(3); // Initialize Router with memoryLimit of 3.
router.addPacket(1, 4, 90); // Packet is added. Return True.
router.addPacket(2, 5, 90); // Packet is added. Return True.
router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
router.addPacket(3, 5, 95); // Packet is added. Return True
router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
router.addPacket(5, 2, 110); // Packet is added. Return True.
router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.
"""


# Solution:;
class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # stores packets in FIFO order
        self.packet_set = set()  # to check duplicates (source, destination, timestamp)
        self.dest_map = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # duplicate check
        if packet in self.packet_set:
            return False

        # evict oldest if over limit
        if len(self.queue) == self.memoryLimit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.packet_set.remove((old_source, old_dest, old_time))
            # remove from destination map
            ts_list = self.dest_map[old_dest]
            # since timestamps were added in increasing order, the first one must match
            if ts_list and ts_list[0] == old_time:
                ts_list.pop(0)
            else:
                # fallback in case order mismatch
                idx = bisect_left(ts_list, old_time)
                if idx < len(ts_list) and ts_list[idx] == old_time:
                    ts_list.pop(idx)

        # add new packet
        self.queue.append(packet)
        self.packet_set.add(packet)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packet_set.remove((source, destination, timestamp))
        ts_list = self.dest_map[destination]
        # first timestamp must match due to increasing insertion order
        if ts_list and ts_list[0] == timestamp:
            ts_list.pop(0)
        else:
            idx = bisect_left(ts_list, timestamp)
            if idx < len(ts_list) and ts_list[idx] == timestamp:
                ts_list.pop(idx)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts_list = self.dest_map[destination]
        if not ts_list:
            return 0
        left = bisect_left(ts_list, startTime)
        right = bisect_right(ts_list, endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)