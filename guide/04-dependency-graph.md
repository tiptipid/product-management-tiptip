# 04 — Dependency Graph & Sequencing

## Why Dependency Pillars: The Fourth Layer

The first three layers (Explore/Exploit → ICE → Kano) answer **what** to build and in **what order**. But they don't answer: **can we build it now?**

A P1 item might depend on a P2 item that hasn't shipped yet. ICE says "build the P1 first," but the dependency says "you can't." Without a sequencing layer, the team picks the highest-scoring item, starts building, and discovers mid-sprint it's blocked.

```mermaid
flowchart TD
    L1["Explore / Exploit<br/>How do we allocate?"]
    L2["ICE Scoring<br/>In what order?"]
    L3["Kano Classification<br/>Any guardrails?"]
    L4["Dependency Pillars<br/>Can we build it now?"]
    OUT["Sprint Commitment"]

    L1 --> L2 --> L3 --> L4 --> OUT

    style L1 fill:#2563EB,color:#fff
    style L2 fill:#F59E0B,color:#000
    style L3 fill:#DC2626,color:#fff
    style L4 fill:#7C3AED,color:#fff
    style OUT fill:#16A34A,color:#fff
```

| Layer | Question | Without It |
|---|---|---|
| **Explore/Exploit** | How to allocate sprints? | Team stagnates or scatters |
| **ICE** | What order to build? | Everything feels equally important |
| **Kano** | Any user-expectation overrides? | Basic features get deprioritized |
| **Dependency Pillars** | Can we build it now? | Team starts items blocked by unshipped dependencies |

> **Example**: Review Nationality Display (P2, ICE=336) scores higher than External Review (P2, ICE=280). ICE says build nationality display first. But nationality display *depends on* review data — External Review must ship first. The dependency layer catches this.

---

## Three Dependency Pillars

Every initiative in the backlog serves one of three strategic pillars. Within each pillar, features depend on each other — building the wrong thing first wastes effort or creates dead-end features.

| Pillar           | Core Question                                                 | NSM Connection                                         |
| ---------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| **🔵 Trust**      | "Will the visitor believe this is safe and legitimate?"       | No trust → no checkout → no bookings                   |
| **🟢 Conversion** | "Can the visitor complete the booking with minimal friction?" | Friction → abandonment → lost bookings                 |
| **🟣 Discovery**  | "Can the visitor find the right experience?"                  | No discovery → no listing views → no checkout attempts |

> **Sequencing Rule**: Trust → Conversion → Discovery. A visitor who finds the perfect listing but doesn't trust the platform won't book. A visitor who trusts the platform but can't checkout as a guest won't book. Fix Trust first, then Conversion, then Discovery.

---

## Trust Chain

```mermaid
flowchart TD
    T1["🔵 Free Cancellation Badge<br/>P0 · ICE 729 · NOW<br/>XS effort"]
    T2["🔵 Locally Curated Badge<br/>Enhancement<br/>P1 · ICE 392 · NOW<br/>S effort"]
    T3["🔵 External Review Import<br/>P2 · ICE 280 · NEXT<br/>On Dev · CONTEX"]
    T4["🔵 Platform Social Proof<br/>Counter<br/>P1 · ICE 448 · NOW<br/>M effort · PAYCOM"]
    T5["🔵 Review Nationality Display<br/>P2 · ICE 336 · NEXT<br/>S effort"]

    T1 --> T2
    T2 --> T3
    T3 --> T5
    T4 -.->|"Needs booking<br/>volume data"| T4note["📊 Data dependency:<br/>requires operational<br/>booking volume"]

    style T1 fill:#16A34A,color:#fff
    style T2 fill:#2563EB,color:#fff
    style T3 fill:#2563EB,color:#fff
    style T4 fill:#2563EB,color:#fff
    style T5 fill:#6B7280,color:#fff
    style T4note fill:#FEF3C7,color:#92400E
```

**Chain Logic:**
- Free Cancel Badge (T1) is a standalone badge — no dependencies, maximum impact per effort
- Locally Curated enhancement (T2) refines the existing badge — builds on T1's visual language
- External Review (T3) imports third-party reviews — needs review data pipeline, which T2's trust context supports
- Social Proof Counter (T4) is independent but requires booking volume data to be meaningful — data dependency, not feature dependency
- Review Nationality Display (T5) depends on External Review data (T3) — can't display nationality without review records

---

## Conversion Chain

```mermaid
flowchart TD
    C1["🟢 Move CTA to Top<br/>P1 · ICE 378 · NOW<br/>XS effort · PAYCOM"]
    C2["🟢 Guest Checkout + SSO<br/>P1 · ICE 405 · NOW<br/>L effort · PAYCOM"]
    C3["🟢 OTP Auth<br/>P2 · ICE 294 · NEXT<br/>M effort · PAYCOM"]
    C4["🟢 Pre-activity Emails<br/>P1 · ICE 392 · NOW<br/>M effort"]
    C5["🟢 Google Pay + Apple Pay<br/>P2 · ICE 256 · NOW<br/>L effort"]
    C6["🟢 I8n Payment / 2C2P<br/>P2 · ICE 160 · NEXT<br/>L effort · PAYCOM"]
    C7["🟢 Package Options<br/>P2 · ICE 294 · NEXT<br/>M effort · CONTEX"]
    C8["🟢 My Booking<br/>P2 · ICE 245 · NEXT<br/>L effort · CONTEX"]
    C9["🟢 Guest Purchase +<br/>My Booking for Guest<br/>P3 · ICE 144 · LATER<br/>XL effort · CONTEX"]

    C1 --> C2
    C2 --> C3
    C2 --> C8
    C2 --> C9
    C5 --> C6
    C4 -.->|"Needs confirmed<br/>booking flow"| C2

    style C1 fill:#16A34A,color:#fff
    style C2 fill:#16A34A,color:#fff
    style C3 fill:#2563EB,color:#fff
    style C4 fill:#2563EB,color:#fff
    style C5 fill:#2563EB,color:#fff
    style C6 fill:#6B7280,color:#fff
    style C7 fill:#2563EB,color:#fff
    style C8 fill:#6B7280,color:#fff
    style C9 fill:#6B7280,color:#fff
```

**Chain Logic:**
- CTA Move (C1) is standalone — quick win, no architecture changes
- SSO / Guest Checkout (C2) is the critical path — it unblocks OTP Auth, My Booking, and Guest Purchase
- OTP Auth (C3) can only be built after SSO architecture is in place (shared auth layer)
- Google/Apple Pay (C5) is independent but 2C2P (C6) builds on the same payment gateway architecture
- Pre-activity Emails (C4) require a confirmed booking to trigger — soft dependency on checkout flow
- Package Options (C7) is independent — can be built by CONTEX in parallel
- My Booking (C8) and Guest Purchase (C9) both depend on auth/SSO (C2)

---

## Discovery Chain

```mermaid
flowchart TD
    D0["🟣 Product Detail<br/>Improvements<br/>✅ Released · CONTEX"]
    D1["🟣 Autocomplete +<br/>Search Filters<br/>P2 · ICE 210 · NEXT<br/>On Dev · CONTEX"]
    D2["🟣 Discover Filter & Sort<br/>P2 · ICE 180 · NEXT<br/>On Dev · CONTEX"]
    D3["🟣 Destination Pages<br/>P2 · ICE 175 · NEXT<br/>Design · CONTEX"]

    D0 --> D1
    D0 --> D2
    D1 --> D3

    style D0 fill:#16A34A,color:#fff
    style D1 fill:#6B7280,color:#fff
    style D2 fill:#6B7280,color:#fff
    style D3 fill:#6B7280,color:#fff
```

**Chain Logic:**
- Product Detail Improvements (D0) is the foundation — already released, listing pages are baseline
- Autocomplete + Filters (D1) and Filter & Sort (D2) can be built in parallel on top of D0
- Destination Pages (D3) need search/filter infrastructure to link to filtered listing views

---

## Cross-Chain Dependencies

Three initiatives depend on features from multiple chains. These are **junction points** that cannot start until their dependencies across chains are met.

```mermaid
flowchart LR
    T3["🔵 External Review<br/>(Trust)"]
    C4["🟢 Pre-activity Email<br/>(Conversion)"]
    C2["🟢 SSO / Guest Checkout<br/>(Conversion)"]
    C8["🟢 My Booking<br/>(Conversion)"]

    X1["⭐ Post-Experience Email<br/>+ Review Request<br/>P2 · ICE 252 · NEXT"]
    X2["⭐ Guest Purchase +<br/>My Booking for Guest<br/>P3 · ICE 144 · LATER"]

    T3 -->|"Review system<br/>must exist"| X1
    C4 -->|"Email infra<br/>must exist"| X1
    C2 -->|"Guest auth<br/>must exist"| X2
    C8 -->|"Booking mgmt<br/>must exist"| X2

    style X1 fill:#F59E0B,color:#000
    style X2 fill:#F59E0B,color:#000
    style T3 fill:#2563EB,color:#fff
    style C4 fill:#16A34A,color:#fff
    style C2 fill:#16A34A,color:#fff
    style C8 fill:#6B7280,color:#fff
```

| Junction Initiative                    | Depends On                                                      | Earliest Start                                    |
| -------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------- |
| Post-Experience Email + Review Request | External Review (Trust) + Pre-activity Email infra (Conversion) | Sprint N+2 (after both chains reach those points) |
| Guest Purchase + My Booking for Guest  | SSO (Conversion) + My Booking (Conversion)                      | Sprint N+3 (after both are shipped)               |

---

## Parallel Sprint Tracks

PAYCOM and CONTEX squads can work their respective chains in parallel. Trust and Conversion are PAYCOM-heavy; Discovery is CONTEX-heavy.

| Sprint  | PAYCOM (Trust + Conversion)                                 | CONTEX (Discovery + Ops)                                                          | Cross-Chain             |
| ------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------- |
| **N**   | 🔵 Free Cancel Badge + 🟢 CTA Move + 🟢 SSO (continue testing) | 🟣 Autocomplete + Filters (continue dev) + 🟣 Discover Filter & Sort (continue dev) | —                       |
| **N+1** | 🔵 Locally Curated Enhancement + 🟢 Pre-activity Emails       | 🔵 External Review (continue dev) + 🟢 Package Options                              | —                       |
| **N+2** | 🔵 Social Proof Counter + 🟢 OTP Auth                         | 🟣 Destination Pages (design → dev) + 🟢 My Booking                                 | —                       |
| **N+3** | 🟢 Google/Apple Pay + 🔵 Review Nationality                   | 🟣 Destination Pages                                                                | ⭐ Post-Experience Email |
| **N+4** | 🟢 2C2P Payment                                              | —                                                                                   | ⭐ Guest Purchase Flow   |

> **Note**: Sprint assignments are illustrative. Actual sprint loading depends on team capacity and velocity. The key constraint is the dependency ordering within each chain — items cannot be reordered without breaking the dependency logic.

---

## Status Legend

| Color         | Meaning                                               |
| ------------- | ----------------------------------------------------- |
| 🟩 Green fill  | P0–P1, NOW horizon — immediate action                 |
| 🟦 Blue fill   | P1–P2, NOW–NEXT — scheduled or in progress            |
| ⬜ Grey fill   | P2–P3, NEXT–LATER — backlogged                        |
| 🟨 Yellow fill | Cross-chain junction — blocked until dependencies met |
| ✅             | Already released                                      |
| Dashed arrow  | Soft dependency (data or infra, not feature)          |
| Solid arrow   | Hard dependency (feature must exist first)            |

---

## When to Generate & Review

The dependency graph is **not a one-time artifact**. It must be reviewed at key moments:

| Trigger | Action | Who |
|---|---|---|
| **New initiative enters backlog** | Assign a Dependency Pillar (Trust / Conversion / Discovery) and identify any blockers | PM |
| **Sprint planning** | Check that all items committed for the sprint have their dependencies met or in-flight | PM + Engineering PIC |
| **Initiative ships** | Mark as Released. Check if any blocked items are now unblocked — promote them for next sprint | PM |
| **Quarterly review** | Regenerate the full dependency graph from the current backlog. Archive the old version. | PM |
| **Initiative invalidated** | Remove from graph and all downstream references. Check if removal unblocks or orphans other items. | PM |

> **Rule of thumb**: If you're unsure whether to update the graph, check the sprint tracks table above. If the current sprint doesn't match the table, the graph is stale.

---

## Where to Track: Backlog Tracker Columns

Dependencies should be tracked **in the Backlog Tracker** (Page 08), not in a separate document. Add the following columns to the tracker sheet:

| Column | Type | Values | Purpose |
|---|---|---|---|
| **Pillar** | Dropdown | `Trust` / `Conversion` / `Discovery` / `—` | Assigns the initiative to a dependency chain. Use `—` for infra or ops items that don't map to a user-facing pillar. |
| **Blocked By** | Text | Initiative name or `—` | Names the specific initiative that must ship first. If none, use `—`. |
| **Blocks** | Text | Initiative name(s) or `—` | Names which downstream initiative(s) this item unblocks when shipped. |

### Example Tracker Rows

| Initiative | Pillar | Blocked By | Blocks |
|---|---|---|---|
| Free Cancellation Badge | Trust | — | Locally Curated Enhancement |
| External Review Import | Trust | Locally Curated Enhancement | Review Nationality Display |
| Guest Checkout + SSO | Conversion | — | OTP Auth, My Booking, Guest Purchase |
| OTP Auth | Conversion | Guest Checkout + SSO | — |
| Autocomplete + Search Filters | Discovery | — | Destination Pages |

### Why Track in the Backlog Tracker

- **Single source of truth** — the team already checks the tracker for ICE, Kano, Horizon, and Explore/Exploit. Adding Pillar + Blocked By keeps all decision dimensions in one view.
- **Filterable** — PM can filter by `Pillar = Trust` to see the full Trust chain, or filter `Blocked By ≠ —` to see all blocked items.
- **Sprint-ready** — during sprint planning, filter `Blocked By = —` AND `Status ≠ Released` to see all items that are ready to pick up.
