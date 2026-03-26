<!-- Part of Java Learning Roadmap — Section 25 -->

# 🗓️ 25. Agile, Scrum & Project Management

---

## 1. Definition

**Agile** is a philosophy of software development focused on delivering code iteratively in small, usable chunks rather than giant, monolithic releases. 
**Scrum** is the most popular framework for *implementing* Agile. It breaks work down into fixed time loops (usually 2-week **Sprints**), driven by a cross-functional team that self-manages to achieve a specific goal.

---

## 2. Why It Exists

Before Agile, companies used the **Waterfall** method:
1. Spend 6 months writing a massive requirements document.
2. Spend 12 months writing the code.
3. Spend 3 months testing it. 
When the software finally launched 2 years later, the market had changed, the competitor won, and the client hated the unchangeable product.
**Agile exists to fail fast and pivot.** By releasing a tiny, working feature every 2 weeks, you get instant customer feedback and can change direction immediately if the feature isn't valuable.

---

## 3. How It Works Internally

### 3.1 The 3 Scrum Roles
1. **Product Owner (PO):** The voice of the business/customer. They write the requirements and prioritize what to build next to maximize revenue.
2. **Scrum Master:** The coach. They run the meetings, protect the engineers from business distractions, and remove "blockers."
3. **Developers:** The engineers (Backend, Frontend, QA) who actually build the increment.

### 3.2 The 4 Ceremonies (The 2-Week Sprint Loop)
1. **Sprint Planning (Monday, Week 1):** The PO says "We need a Checkout Cart." The Devs look at the backlog, estimate how hard it is, and pull just enough work they can guarantee to finish in 2 weeks.
2. **Daily Standup (Every Day):** A strict 15-minute sync. "What did I do yesterday? What am I doing today? Am I blocked by anything?"
3. **Sprint Review (Friday, Week 2):** The Devs demo the *functioning, live software* to the business stakeholders.
4. **Sprint Retrospective (Friday, Week 2):** A private team meeting. "What went well? What was terrible? How do we improve our process for the next Sprint?"

---

## 4. Ticket Organization Examples

Work is tracked in tools like **Jira**.

### 4.1 Hierarchy of Work
*   **Epic:** A massive 3-month project. (e.g., `Integrate Stripe Payments`)
*   **User Story:** A piece of the Epic that delivers 1 piece of value in 1 Sprint. (e.g., `Add Credit Card UI Form`)
*   **Bug:** Code is broken. (e.g., `Submit button crashes on Visa cards`)
*   **Task/Spike:** Backend technical work with no immediate UI value. (e.g., `Research Stripe Java API SDK`)

### 4.2 The Golden User Story Format
A perfect Jira ticket is written from the user's perspective, not the database's perspective.
> **Title:** `As a Customer, I want to see my Order History so I can track my shipping.`
> **Acceptance Criteria (Definition of Done):**
> 1. Given I am logged in, when I click 'History', I see a list of my past 5 orders.
> 2. The list must show the Order Date, Total Price, and Status.
> 3. If I have no orders, show "No orders found."

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| What is "Story Pointing" (Estimation)? | Instead of estimating work in Hours (which developers notoriously underestimate), teams use abstract "Points" (usually the Fibonacci sequence: 1, 2, 3, 5, 8). A "3" is medium effort. An "8" means it's incredibly complex and needs to be broken down into smaller tickets. |
| What is Team Velocity? | The average number of Story Points a team successfully finishes in a Sprint over time. If a team's velocity is 40 points, the PO knows they cannot cram 80 points of work into the next Sprint. |
| What do you do if you finish all your Sprint tickets early? | You don't just sit idle. You ask the Product Owner what the highest priority ticket at the top of the overall Backlog is, and pull it into the current Sprint. |
| What is a "Blocker"? | Anything preventing an engineer from continuing their work. (e.g., Waiting on the DevOps team to provision a database). You announce this in the Daily Standup so the Scrum Master can fight the battle to unblock you. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| The 45-Minute Daily Standup | Standup turns into a highly technical architecture debate between two senior engineers, wasting the time of the other 6 people in the room. | Answer the 3 questions strictly. If a debate starts, the Scrum Master yells "Take it offline!" and those two engineers stay after the meeting to discuss it privately. |
| "Agile" means "No Documentation" | Because the Manifesto says "Working software over comprehensive documentation," teams write zero technical specs or flowcharts, resulting in chaotic codebases. | The manifesto says value *over* documentation, not *exclude* documentation. Complex HLDs and API contracts must still be firmly documented. |
| Rolling over tickets constantly | An 8-point ticket isn't finished. It gets pushed to the next sprint. Then the next sprint. It takes 6 weeks. | The ticket was too large to begin with. An Epic was disguised as a Story. The PO needs to break it down. |

---

## 7. Real-World Usage

| Tool / Practice | Where it shows up |
|---|---|
| **Jira Software** | The absolute industry standard. It features the "Scrum Board" (To Do -> In Progress -> In Code Review -> Testing -> Done). Every Git branch branch is usually named after the Jira ticket (e.g., `git checkout -b feature/PROJ-412-checkout-button`). |
| **Burndown Chart** | A graph mapped on the wall. Day 1 starts with 40 points of work. As tickets move to "Done", the graph burns down. If there are 3 days left in the Sprint and the graph is still hovering at 30 points, the team knows they are severely behind schedule. |
| **Planning Poker** | During Sprint Planning, the team discusses a ticket. Everyone secretly picks a Fibonacci card (1, 2, 3, 5, 8). Everyone reveals at the same time. If Alice picks 2, and Bob picks 8, they must debate *why* their estimates are so drastically different before agreeing on a group consensus. |

---

## 8. Practice Tasks

1.  **Write a User Story:** Pick an app you use daily (e.g., Uber). Write a proper Jira-style User Story for the feature "Add a tip to the driver". Include the "As a... I want... So that..." format, and write exactly 3 strict Acceptance Criteria it must pass to be considered "Done."
2.  **Scrum Master Simulation:** You are in a daily standup. A junior developer says, "I've been stuck trying to connect to the AWS Database for 3 days." As a teammate or Scrum Master, what is the exact next step you take immediately after the meeting?

---

## 9. Quick Revision

### The Scrum Workflow
1.  **Backlog Refinement:** PO makes sure tickets are clear.
2.  **Sprint Planning:** Devs commit to a chunk of points for the next 2 weeks.
3.  **Daily Standup:** Daily 15-minute sync-up.
4.  **Sprint Review:** Demo the finished code to the business.
5.  **Retrospective:** Team complains about what broke and fixes the process.

### The Artifacts
*   **Product Backlog:** All the giant ideas we eventually want to build.
*   **Sprint Backlog:** The specific tickets we are building *right now*.
*   **Increment:** The 100% finished, tested, integrated code ready to go to Production.
