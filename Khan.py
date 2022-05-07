Skip to content

GitLab

Toggle navigation Menu 

Data

Data

Project information

Repository

Files

Commits

Branches

Tags

Contributors

Graph

Compare

Locked Files

Issues

135

Merge requests

46

CI/CD

Deployments

External wiki

Close sidebar

 GitLab 15.0 is launching on May 22! This version brings many exciting improvements, but also removes deprecated features and introduces breaking changes that may impact your workflow. To see what is being deprecated and removed, please visit Breaking changes in 15.0 and Deprecations. 

Open sidebar

F-Droid

DataData

Repository

master

fdroiddata

metadata

com.termux.yml

com.termux.yml

14.08 KiB

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

337

338

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

361

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

384

385

386

387

388

389

390

391

392

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

452

453

454

455

456

457

458

459

460

461

462

463

464

465

466

467

468

469

470

471

472

473

474

475

476

477

478

479

480

481

482

483

484

485

486

487

488

489

490

491

492

493

494

495

496

497

498

499

500

501

502

503

504

505

506

507

508

509

510

511

512

513

514

515

516

517

518

519

520

521

522

523

524

525

526

527

528

529

530

531

532

533

534

535

536

537

538

539

540

541

542

543

544

545

546

547

548

549

550

551

552

553

554

555

556

557

558

559

560

561

562

563

564

565

566

567

568

569

570

571

572

573

574

575

576

577

578

579

580

581

582

583

584

585

586

587

588

589

590

591

592

593

594

595

596

597

598

599

600

601

602

603

604

605

606

607

608

609

610

611

612

613

614

615

616

617

618

619

620

621

622

623

624

625

626

627

628

629

630

631

632

633

634

635

636

637

638

639

640

641

642

643

644

645

646

647

648

649

650

651

652

653

654

655

656

657

658

659

660

661

662

663

664

665

666

667

668

669

670

671

672

673

674

675

676

677

678

679

680

681

682

683

684

685

686

687

688

689

690

691

692

693

694

695

696

697

698

699

700

701

702

703

704

705

706

707

708

709

710

711

712

713

714

715

716

717

718

719

720

721

722

723

724

725

726

727

728

729

730

731

732

733

734

735

736

737

738

739

740

741

742

743

744

745

746

747

748

749

750

751

752

753

754

755

756

757

758

759

760

761

762

763

764

765

766

767

768

769

770

771

772

773

774

775

776

Categories:

  - Development

License: GPL-3.0-only

WebSite: https://termux.com

SourceCode: https://github.com/termux/termux-app

IssueTracker: https://github.com/termux/termux-app/issues

Changelog: https://github.com/termux/termux-app/releases

Donate: https://termux.com/donate.html

Bitcoin: 1BXS5qPhJzhr5iK5nmNDSmoLDfB6VmN5hv

AutoName: Termux

Description: |-

    Termux combines powerful terminal emulation with an extensive Linux package

    collection.

    * Enjoy the bash and zsh shells.

    * Edit files with nano and vim.

    * Access servers over ssh.

    * Compile code with gcc and clang.

    * Use the python console as a pocket calculator.

    * Check out projects with git and subversion.

    * Run text-based games with frotz.

    At first start a small base system is downloaded - desired packages can then be

    installed using the apt package manager known from the Debian and Ubuntu Linux

    distributions. Access the built-in help by long-pressing anywhere on the

    terminal and selecting the Help menu option to learn more.

    Read help online: <a href="https://wiki.termux.com/">https://wiki.termux.com/</a>

    Reddit Community: <a href="https://termux.com/community">https://termux.com/community</a>

RepoType: git

Repo: https://github.com/termux/termux-app

Builds:

  - versionName: '0.16'

    versionCode: 16

    commit: dea7c9d2ceb3060c

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.17'

    versionCode: 17

    commit: v0.17

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.18'

    versionCode: 18

    commit: v0.18

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.19'

    versionCode: 19

    commit: v0.19

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.20'

    versionCode: 20

    commit: v0.20

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.21'

    versionCode: 21

    commit: v0.21

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.22'

    versionCode: 22

    commit: v0.22

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.23'

    versionCode: 23

    commit: v0.23

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.24'

    versionCode: 24

    commit: v0.24

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.25'

    versionCode: 25

    commit: v0.25

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.26'

    versionCode: 26

    commit: v0.26

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.27'

    versionCode: 27

    commit: v0.27

    subdir: app

    gradle:

      - yes

    scandelete:

      - app/src/main/jniLibs

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.28'

    versionCode: 28

    commit: v0.28

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.29'

    versionCode: 29

    commit: v0.29

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.30'

    versionCode: 30

    commit: v0.30

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.31'

    versionCode: 31

    commit: v0.31

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.32'

    versionCode: 32

    commit: v0.32

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.33'

    versionCode: 33

    commit: v0.33

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.34'

    versionCode: 34

    commit: v0.34

    subdir: app

    gradle:

      - yes

    build:

      - cd ..

      - ./build-jnilibs.sh

  - versionName: '0.35'

    versionCode: 36

    commit: v0.35

    subdir: app

    gradle:

      - yes

  - versionName: '0.37'

    versionCode: 37

    commit: v0.37

    subdir: app

    gradle:

      - yes

  - versionName: '0.38'

    versionCode: 38

    commit: v0.38

    subdir: app

    gradle:

      - yes

  - versionName: '0.39'

    versionCode: 39

    commit: v0.39

    subdir: app

    gradle:

      - yes

  - versionName: '0.40'

    versionCode: 40

    commit: v0.40

    subdir: app

    gradle:

      - yes

  - versionName: '0.41'

    versionCode: 41

    commit: v0.41

    subdir: app

    gradle:

      - yes

  - versionName: '0.42'

    versionCode: 42

    commit: v0.42

    subdir: app

    gradle:

      - yes

  - versionName: '0.44'

    versionCode: 44

    commit: v0.44

    subdir: app

    gradle:

      - yes

  - versionName: '0.45'

    versionCode: 45

    commit: v0.45

    subdir: app

    gradle:

      - yes

  - versionName: '0.46'

    versionCode: 46

    commit: v0.46

    subdir: app

    gradle:

      - yes

  - versionName: '0.47'

    versionCode: 47

    commit: v0.47

    subdir: app

    gradle:

      - yes

  - versionName: '0.48'

    versionCode: 48

    commit: v0.48

    subdir: app

    gradle:

      - yes

  - versionName: '0.49'

    versionCode: 49

    disable: fdroid/fdroidserver#288

    commit: v0.49

    subdir: app

    gradle:

      - yes

  - versionName: '0.50'

    versionCode: 50

    commit: v0.50

    subdir: app

    gradle:

      - yes

  - versionName: '0.51'

    versionCode: 51

    commit: v0.51

    subdir: app

    gradle:

      - yes

  - versionName: '0.52'

    versionCode: 52

    commit: v0.52

    subdir: app

    gradle:

      - yes

  - versionName: '0.53'

    versionCode: 53

    commit: v0.53

    subdir: app

    gradle:

      - yes

  - versionName: '0.54'

    versionCode: 54

    commit: v0.54

    subdir: app

    gradle:

      - yes

  - versionName: '0.55'

    versionCode: 55

    commit: v0.55

    subdir: app

    gradle:

      - yes

  - versionName: '0.56'

    versionCode: 56

    commit: v0.56

    subdir: app

    gradle:

      - yes

  - versionName: '0.57'

    versionCode: 57

    commit: v0.57

    subdir: app

    gradle:

      - yes

  - versionName: '0.59'

    versionCode: 59

    commit: v0.59

    subdir: app

    gradle:

      - yes

  - versionName: '0.60'

    versionCode: 60

    commit: v0.60

    subdir: app

    gradle:

      - yes

  - versionName: '0.61'

    versionCode: 61

    commit: v0.61

    subdir: app

    gradle:

      - yes

  - versionName: '0.62'

    versionCode: 62

    commit: v0.62

    subdir: app

    gradle:

      - yes

  - versionName: '0.63'

    versionCode: 63

    commit: v0.63

    subdir: app

    gradle:

      - yes

  - versionName: '0.64'

    versionCode: 64

    commit: v0.64

    subdir: app

    gradle:

      - yes

  - versionName: '0.65'

    versionCode: 65

    commit: v0.65

    subdir: app

    gradle:

      - yes

  - versionName: '0.66'

    versionCode: 66

    commit: v0.66

    subdir: app

    gradle:

      - yes

  - versionName: '0.67'

    versionCode: 67

    commit: v0.67

    subdir: app

    gradle:

      - yes

  - versionName: '0.68'

    versionCode: 68

    commit: v0.68

    subdir: app

    gradle:

      - yes

  - versionName: '0.69'

    versionCode: 69

    commit: v0.69

    subdir: app

    gradle:

      - yes

  - versionName: '0.70'

    versionCode: 70

    commit: v0.70

    subdir: app

    gradle:

      - yes

  - versionName: '0.71'

    versionCode: 71

    commit: v0.71

    subdir: app

    gradle:

      - yes

  - versionName: '0.72'

    versionCode: 72

    commit: v0.72

    subdir: app

    gradle:

      - yes

  - versionName: '0.73'

    versionCode: 73

    commit: v0.73

    subdir: app

    gradle:

      - yes

  - versionName: '0.74'

    versionCode: 74

    commit: v0.74

    subdir: app

    gradle:

      - yes

  - versionName: '0.75'

    versionCode: 75

    commit: v0.75

    subdir: app

    gradle:

      - yes

  - versionName: '0.76'

    versionCode: 76

    commit: v0.76

    subdir: app

    gradle:

      - yes

  - versionName: '0.77'

    versionCode: 77

    commit: v0.77

    subdir: app

    gradle:

      - yes

  - versionName: '0.82'

    versionCode: 82

    commit: v0.82

    subdir: app

    gradle:

      - yes

  - versionName: '0.84'

    versionCode: 84

    commit: v0.84

    subdir: app

    gradle:

      - yes

  - versionName: '0.86'

    versionCode: 86

    commit: v0.86

    subdir: app

    gradle:

      - yes

  - versionName: '0.88'

    versionCode: 88

    commit: v0.88

    subdir: app

    gradle:

      - yes

  - versionName: '0.90'

    versionCode: 90

    commit: v0.90

    subdir: app

    gradle:

      - yes

  - versionName: '0.92'

    versionCode: 92

    commit: v0.92

    subdir: app

    gradle:

      - yes

  - versionName: '0.94'

    versionCode: 94

    commit: v0.94

    subdir: app

    gradle:

      - yes

    ndk: r21

  - versionName: '0.95'

    versionCode: 95

    commit: v0.95

    subdir: app

    gradle:

      - yes

    prebuild: sed -i -e 's/21.2.6472646/21.3.6528147/' build.gradle

    ndk: r21d

  - versionName: '0.96'

    versionCode: 96

    commit: v0.96

    subdir: app

    gradle:

      - yes

    prebuild: sed -i -e 's/21.2.6472646/21.3.6528147/' build.gradle

    ndk: r21d

  - versionName: '0.99'

    versionCode: 99

    commit: v0.99

    subdir: app

    gradle:

      - yes

    ndk: r21d

  - versionName: '0.101'

    versionCode: 101

    commit: v0.101

    subdir: app

    gradle:

      - yes

    ndk: r21d

  - versionName: '0.102'

    versionCode: 102

    commit: v0.102

    subdir: app

    gradle:

      - yes

    ndk: r21d

  - versionName: '0.103'

    versionCode: 103

    commit: v0.103

    subdir: app

    gradle:

      - yes

    ndk: r21d

  - versionName: '0.104'

    versionCode: 104

    commit: v0.104

    subdir: app

    gradle:

      - yes

    ndk: r21d

  - versionName: '0.105'

    versionCode: 105

    disable: crash on start upstream issue 1896

    commit: v0.105

    subdir: app

    gradle:

      - yes

    ndk: r22

  - versionName: '0.106'

    versionCode: 106

    commit: v0.106

    subdir: app

    gradle:

      - yes

    ndk: r22

  - versionName: '0.107'

    versionCode: 107

    commit: v0.107

    subdir: app

    gradle:

      - yes

    prebuild: sed -i -e '/splits\ {/,+8d' build.gradle

    ndk: r22

  - versionName: '0.108'

    versionCode: 108

    commit: v0.108

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/splits\ {/,+8d' build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../terminal-{emulator,view}/build.gradle

    ndk: r22

  - versionName: '0.111'

    versionCode: 111

    commit: v0.111

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/splits\ {/,+8d' build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../termux-shared/build.gradle

      - sed -i -e 's/22.0.7026061/22.1.7171670/' ../gradle.properties

    ndk: r22b

  - versionName: '0.112'

    versionCode: 112

    commit: v0.112

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/splits\ {/,+8d' build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../termux-shared/build.gradle

      - sed -i -e 's/22.0.7026061/22.1.7171670/' ../gradle.properties

    ndk: r22b

  - versionName: '0.113'

    versionCode: 113

    commit: v0.113

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/splits\ {/,+8d' build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../termux-shared/build.gradle

      - sed -i -e 's/22.0.7026061/22.1.7171670/' ../gradle.properties

    ndk: r22b

  - versionName: '0.114'

    versionCode: 114

    commit: v0.114

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/splits\ {/,+8d' build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^}/d' ../termux-shared/build.gradle

      - sed -i -e 's/22.0.7026061/22.1.7171670/' ../gradle.properties

    ndk: r22b

  - versionName: '0.115'

    versionCode: 115

    commit: bde9d01f766d70007f82d34a68122fc34aa1afe5

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/publishing {/,/^    }/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^    }/d' ../termux-shared/build.gradle

    ndk: r22b

  - versionName: '0.116'

    versionCode: 116

    commit: 78be0e793eba633f5a3278f20681983877341f7a

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/publishing {/,/^    }/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^    }/d' ../termux-shared/build.gradle

    ndk: r22b

  - versionName: '0.117'

    versionCode: 117

    commit: 9272a757affc0dae4aa044248800f3987e06c52b

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/publishing {/,/^    }/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^    }/d' ../termux-shared/build.gradle

    ndk: r22b

  - versionName: 0.118.0

    versionCode: 118

    commit: 6e2689f55295fa444be8ac8592c527c2c5ef3253

    subdir: app

    gradle:

      - yes

    prebuild:

      - sed -i -e '/publishing {/,/^    }/d' ../terminal-{emulator,view}/build.gradle

      - sed -i -e '/publishing {/,/^    }/d' ../termux-shared/build.gradle

    ndk: r22b

AutoUpdateMode: Version v%v

UpdateCheckMode: Tags

CurrentVersion: 0.118.0

CurrentVersionCode: 118
